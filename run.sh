#!/bin/bash

# Edit this to the location of your jinja2-live parser code
#JLP_HOME=~gmatz/Code/jinja2-live-parser

#cd $JLP_HOME
#exec python parser.py
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
ln -s ../venv/lib/python2.7/site-packages/ansible/runner/filter_plugins filters/ansible
python parser.py
