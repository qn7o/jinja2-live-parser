# Jinja2 live parser

A lightweight live parser for [Jinja2](http://jinja.pocoo.org/docs/dev/) based on [Flask](http://flask.pocoo.org/) and [Jquery](http://jquery.com/).  
All you need is Python and preferably [pip](https://pypi.python.org/pypi/pip). Can parse JSON and YAML inputs.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Install

### Clone + pip

    $ git clone git@github.com:abourguignon/jinja2-live-parser.git
    $ pip install -r requirements.txt
    $ python parser.py

### Dockerfile

Build it:

    docker build -t mydocker/j2parser .
    docker run -d -p 5000:5000 mydocker/j2parser

Or simply pull it from registry (without building):

    docker run -d -p 5000:5000 sahilsk/j2parser


## Usage

You are all set, go to `http://localhost:5000/` and have fun.  
You can add any custom filter you'd like in `filters.py`.  Just make sure the function's name starts with `filter_`.


## Preview

![preview](http://i.imgur.com/T65xjAf.png)
