#!/usr/bin/env bash

# setting -e to exit immediately on a command failure.
# setting -o pipefail sets the exit code of a pipeline to that of the rightmost command to exit with a non-zero status, or to zero if all commands of the pipeline exit successfully.
set -eo pipefail

if [ -z "$VIRTUAL_ENV" ]; then
    echo "warning: you are not in a virtualenv"
    exit 1
fi

pip install pip pip-tools
pip-compile requirements.in
pip-compile dev_requirements.in
pip-sync requirements.txt test_requirements.txt dev_requirements.txt

