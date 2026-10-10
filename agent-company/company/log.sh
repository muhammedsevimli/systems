#!/usr/bin/env bash
# Writes one line to the company log. It always writes to company/log.jsonl in the main folder,
# even when a worker calls it from their own desk.
# Usage: bash company/log.sh <who> <event> "<detail>"
# Events: setup hire desk start helper finish merge approval_request approved rejected stopped
set -e

if [ "$#" -lt 3 ]; then
  echo "usage: bash company/log.sh <who> <event> \"<detail>\"" >&2
  exit 1
fi

who="$1"
event="$2"
shift 2
detail="$*"

case "$event" in
  setup|hire|desk|start|helper|finish|merge|approval_request|approved|rejected|stopped) ;;
  *) echo "unknown event: $event" >&2; exit 1 ;;
esac

common="$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null || true)"
if [ -n "$common" ]; then
  root="$(cd "$common/.." && pwd)"
else
  root="$(cd "$(dirname "$0")/.." && pwd)"
fi

escape() {
  printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g' | tr '\r\n\t' '   '
}

t="$(date -Iseconds)"
printf '{"t":"%s","who":"%s","event":"%s","detail":"%s"}\n' \
  "$t" "$(escape "$who")" "$(escape "$event")" "$(escape "$detail")" >> "$root/company/log.jsonl"
