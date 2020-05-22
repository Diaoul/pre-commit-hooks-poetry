#!/usr/bin/env bash
poetry export --format requirements.txt --output "$@"
