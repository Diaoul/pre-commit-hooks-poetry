#!/usr/bin/env bash
if [ -n "${DEBUG}" ]; then
  set -x
fi
poetry export --format requirements.txt --output "$@"
