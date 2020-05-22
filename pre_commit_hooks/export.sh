#!/bin/sh
poetry export --format requirements.txt --output "$@"
