#!/usr/bin/env bash
if [ -n "${DEBUG}" ]; then
  set -x
fi

poetry export --format requirements.txt "${@: 1:$#-1}" --output "${@: -1}"
