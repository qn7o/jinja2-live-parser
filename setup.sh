#!/bin/bash

pip install virtualenv
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
ln -s ../venv/lib/python2.7/site-packages/ansible/runner/filter_plugins filters/ansible
