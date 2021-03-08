#!/bin/bash
set -e

git clean -fd
git reset --hard
# branch=$(git branch | grep '*' | awk '{ print $2 }')
git_c () {
  ssh-agent bash -c "ssh-add /root/keys_gh/gh; $1"
}
# git_c "git pull origin $branch"
git_c "git pull origin develop-deploy_setup"
git_c "git checkout develop-deploy_setup"

echo Installing requirements via pip...
pip3 install -r requirements.txt

echo Creating a virtual environment...
virtualenv venv

echo Activating the virtual environment...
source ./venv/bin/activate

echo Launching the API server...
python3 api.py