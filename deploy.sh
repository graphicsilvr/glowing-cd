#!/bin/bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/dokey2
git pull
systemctl restart my-application

