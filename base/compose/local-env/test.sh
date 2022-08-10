#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py wait_for_db && sleep 2m

echo 'Running Test suite.....'
pytest

echo 'Populating coverage report....'
coverage run --rcfile=.coveragerc -m pytest
coverage report

echo 'Populating html coverage report....'
coverage html -d templates/htmlcov

echo 'Running Static linting.....'
# pylint -j 4 wrike tasks user
