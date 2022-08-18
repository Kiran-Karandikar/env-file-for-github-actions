#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

mkdir -p .envs/.local


#touch .envs/.local/.sample
#echo SECRET_1='${{ secrets.SECRET_1 }}' >> .envs/.local/.sample
## shellcheck disable=SC2016
#echo SECRET_2='${{ secrets.SECRET_2 }}' >> .envs/.local/.sample
#cat .envs/.local/.sample
