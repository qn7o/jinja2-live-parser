# -*- coding: utf-8 -*-
import os
import sys
import json
import yaml
import logging

from flask import Flask, render_template, request
from jinja2 import Template, Environment, meta, exceptions
from random import choice

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    dummy_values = [ 'Lorem', 'Ipsum', 'Amet', 'Elit', 'Expositum', 
        'Dissimile', 'Superiori', 'Laboro', 'Torquate', 'sunt', 
    ]
    # Check if template have no errors
    try:
        tpl = Template(request.form['template'])
    except (exceptions.TemplateSyntaxError, exceptions.TemplateError) as e:
        return "Syntax error in jinja2 template: {0}".format(e)
    values = {}

    if bool(int(request.form['dummyvalues'])):
        # List variables (introspection)
        env = Environment()
        vars_to_fill = meta.find_undeclared_variables(env.parse(request.form['template']))

        for v in vars_to_fill:
            values[v] = choice(dummy_values)
    else:
        # Check JSON for errors
        if request.form['input_type'] == "json":
            try:
                values = json.loads(request.form['values'])
            except ValueError as e:
                return "Value error in JSON: {0}".format(e)
        # Check YAML for errors
        elif request.form['input_type'] == "yaml":
            try:
                values = yaml.load(request.form['values'])
            except (ValueError, yaml.parser.ParserError, TypeError) as e:
                return "Value error in YAML: {0}".format(e)
        else:
            return "Undefined input_type: {0}".format(request.form['input_type'])

    # If ve have empty var array or other errors we need to catch it and show
    try:
        rendered_tpl = tpl.render(values)
    except (ValueError, TypeError) as e:
        return "Error in your values input filed: {0}".format(e)

    if bool(int(request.form['showwhitespaces'])):
        # Replace whitespaces with a visible character (will be grayed with javascript)
        rendered_tpl = rendered_tpl.replace(' ', u'•')

    return rendered_tpl.replace('\n', '<br />')

def save_log(logfile=None):
    """Save parser log """
    logname = logfile if logfile else "parser.log"
    cwd = os.path.dirname(os.path.realpath(__file__))
    logdir = os.path.join(cwd, "log")
    
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    
    logpath = os.path.join(logdir, logname)
    logging.basicConfig(filename=logpath, level=logging.DEBUG)

def server(debug=True, logfile=None):
    # Set service runing as daemon
    if debug is not True:
        if 0 != os.fork():
            sys.exit(0)
            os.setsid()

    save_log(logfile)
    app.debug = debug
    app.run(host='0.0.0.0', port=8089)

if __name__ == "__main__":
    server(debug=False)
