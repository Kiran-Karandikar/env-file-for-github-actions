#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo 'Running Test suite.....'
pytest
