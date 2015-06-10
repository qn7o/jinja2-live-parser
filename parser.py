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
    tpl = Template(request.form.get('template'))
    values = request.form.get('values')
    try:
        values = json.loads(values) if values else {}
    except:
        return 'Invalid JSON!'

    rendered_tpl = tpl.render(values)

    if bool(int(request.form['showwhitespaces'])):
        # Replace whitespaces with a visible character (will be grayed with
        # javascript)
        rendered_tpl = rendered_tpl.replace(' ', u'•')

    return rendered_tpl.replace('\n', '<br />')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
