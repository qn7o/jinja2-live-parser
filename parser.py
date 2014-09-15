# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from jinja2 import Template, Environment, meta
from random import choice
import json


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    dummy_values = [ 'Lorem', 'Ipsum', 'Amet', 'Elit', 'Expositum', 
        'Dissimile', 'Superiori', 'Laboro', 'Torquate', 'sunt', 
    ]

    tpl = Template(request.form['template'])
    values = {}

    if bool(int(request.form['dummyvalues'])):
        # List variables (introspection)
        env = Environment()
        vars_to_fill = meta.find_undeclared_variables(env.parse(request.form['template']))

        for v in vars_to_fill:
            values[v] = choice(dummy_values)
    else:
        values = json.loads(request.form['values'])

    rendered_tpl = tpl.render(values)

    if bool(int(request.form['showwhitespaces'])):
        # Replace whitespaces with a visible character (will be grayed with javascript)
        rendered_tpl = rendered_tpl.replace(' ', u'•')

    return rendered_tpl.replace('\n', '<br />')


if __name__ == "__main__":
    app.debug = True
    app.run()
