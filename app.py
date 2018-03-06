#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:43:03 2018

@author: johnnyhsieh
"""

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from ENS import check
import os
DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('ENS:', validators=[validators.Length(min=7)
    ,validators.optional(strip_whitespace=False)])





@app.route("/", methods=['POST','GET'])
def search_ENS():
    form = ReusableForm(request.form)

    print(form.errors)

    if request.method == 'POST':
        name=request.form['name']
        name = name.replace(" ","")


        if form.validate():
            # Save the comment here.
            print(name + " Owner Status: " + check(name))
            flash(name + " Owner Status: " + check(name))
        else:
            flash('ENS need to greater than 7 charaters.')

    return render_template('index.html', form=form)

@app.route("/GET", methods=['GET'])
def get_ENS():
    form = ReusableForm(request.form)

    print(form.errors)


    if request.method == 'GET':

        name=request.args.get('name')
        print(name)

        if form.validate():
            # Save the comment here.
            flash(name + " Owner Status: " + check(name))
            print(name + " Owner Status: " + check(name))
            print(check(name))
            return check(name)
        else:
            flash('ENS need to greater than 7 charaters.')
            return 'ENS need to greater than 7 charaters.'



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0',port = port, debug=True)
