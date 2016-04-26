# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import Flask, render_template, request
from jinja2 import Template, Environment, meta, exceptions
from random import choice
import logging
import logging.handlers
import json
import yaml
import config


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


if __name__ == "__main__":
    # Set up logging
    app.logger.setLevel(logging.__getattribute__(config.LOGGING_LEVEL))
    file_handler = logging.handlers.RotatingFileHandler(filename=config.LOGGING_LOCATION, maxBytes=10*1024*1024, backupCount=5)
    file_handler.setFormatter(logging.Formatter(config.LOGGING_FORMAT))
    file_handler.setLevel(logging.__getattribute__(config.LOGGING_LEVEL))
    app.logger.addHandler(file_handler)

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
    )
