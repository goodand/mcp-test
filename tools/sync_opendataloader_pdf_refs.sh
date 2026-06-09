#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(git rev-parse --show-toplevel)}"
SRC="$ROOT/third_party/repos/opendataloader_pdf"
DST="$ROOT/third_party/references/opendataloader-pdf"

mkdir -p "$DST"

cp "$SRC/schema.json" "$DST/schema.json"
cp "$SRC/options.json" "$DST/options.json"

echo "Synced opendataloader-pdf references:"
echo "  $DST/schema.json"
echo "  $DST/options.json"
