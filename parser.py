# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import Flask, render_template, request
from jinja2 import Environment, meta, exceptions
from random import choice
from inspect import getmembers, isfunction
from cgi import escape
import logging
import logging.handlers
import json
import yaml
import config


app = Flask(__name__)


def get_custom_filters():
    import filters
    custom_filters = {}
    for m in getmembers(filters):
        if m[0].startswith('filter_') and isfunction(m[1]):
            filter_name = m[0][7:]
            custom_filters[filter_name] = m[1]

    return custom_filters


@app.route("/")
def home():
    return render_template('index.html', custom_filters=get_custom_filters())


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    jinja2_env = Environment(extensions=['jinja2.ext.do'])

    # Load custom filters
    custom_filters = get_custom_filters()
    app.logger.debug('Add the following customer filters to Jinja environment: %s' % ', '.join(custom_filters.keys()))
    jinja2_env.filters.update(custom_filters)

    # Load the template
    try:
        jinja2_tpl = jinja2_env.from_string(request.form['template'])
    except (exceptions.TemplateSyntaxError, exceptions.TemplateError) as e:
        return "Syntax error in jinja2 template: {0}".format(e)


    dummy_values = [ 'Lorem', 'Ipsum', 'Amet', 'Elit', 'Expositum',
        'Dissimile', 'Superiori', 'Laboro', 'Torquate', 'sunt',
    ]
    values = {}
    if bool(int(request.form['dummyvalues'])):
        # List template variables (introspection)
        vars_to_fill = meta.find_undeclared_variables(jinja2_env.parse(request.form['template']))

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
        rendered_jinja2_tpl = jinja2_tpl.render(values)
    except (ValueError, TypeError) as e:
        return "Error in your values input filed: {0}".format(e)

    if bool(int(request.form['showwhitespaces'])):
        # Replace whitespaces with a visible character (will be grayed with javascript)
        rendered_jinja2_tpl = rendered_jinja2_tpl.replace(' ', u'•')

    return escape(rendered_jinja2_tpl).replace('\n', '<br />')


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
