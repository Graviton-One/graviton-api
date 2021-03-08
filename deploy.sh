#!/bin/bash
set -e

git clean -fd
git reset --hard
branch=$(git branch | grep '*' | awk '{ print $2 }')

git_c () {
  ssh-agent bash -c "ssh-add /root/keys_gh/gh; $1"
}

git_c "git pull origin $branch"

#echo Installing venv...
#apt install python3-venv

#echo Creating a virtual environment...
#python3 -m venv venv 

#echo Activating the virtual environment...
#source ./venv/bin/activate

echo Installing requirements via pip...
pip3 install -r requirements.txt

echo Relaunching the systemd server...
systemctl restart graviton-api.service