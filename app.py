#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.fields.html5 import DateField

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

class TestForm(FlaskForm):
    now = DateField(u'Current time', format='%m/%d/%Y')
    submit = SubmitField(u'Submit')

app = create_app()

@app.route('/', methods=['post', 'get'])
def index():
    form = TestForm(csrf_enabled=False)

    if form.validate_on_submit():
        return form.now.data.strftime('%x')
    return render_template('index.html', form=form)
