# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from jinja2 import Template, Environment, meta
from random import choice
import json
# For dynamic loading of filters
import imp
from inspect import getmembers, isfunction
import os

app = Flask(__name__)

# Load filters in filters dir
filter_path='filters'
for filter in os.listdir(filter_path):
    if not os.path.isfile(os.path.join(filter_path, filter)):
        continue
    else:
        mod_name,file_ext = os.path.splitext(os.path.split(filter)[-1])
        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, os.path.join(filter_path, filter))
            for name, function in getmembers(py_mod):
                    if isfunction(function):
                        app.jinja_env.filters[name] = function

@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    dummy_values = [ 'Lorem', 'Ipsum', 'Amet', 'Elit', 'Expositum', 
        'Dissimile', 'Superiori', 'Laboro', 'Torquate', 'sunt', 
    ]

    tpl = app.jinja_env.from_string(request.form['template'])
    values = {}

    if int(request.form['dummyvalues']):
        # List variables (introspection)
        env = Environment()
        vars_to_fill = meta.find_undeclared_variables(env.parse(request.form['template']))

        for v in vars_to_fill:
            values[v] = choice(dummy_values)
    else:
        values = json.loads(request.form['values'])

    rendered_tpl = tpl.render(values)

    if int(request.form['showwhitespaces']):
        # Replace whitespaces with a visible character (will be grayed with javascript)
        rendered_tpl = rendered_tpl.replace(' ', u'•')

    return rendered_tpl.replace('\n', '<br />')

if __name__ == "__main__":
    app.debug = True
    app.run()
