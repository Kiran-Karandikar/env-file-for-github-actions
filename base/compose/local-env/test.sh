#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo 'Running Test suite.....'
pytest

echo 'Populating coverage report....'
coverage run --rcfile=.coveragerc -m pytest
coverage report

echo 'Populating html coverage report....'
coverage html -d templates/htmlcov

