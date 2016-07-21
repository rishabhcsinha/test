from flask import render_template, session, flash, request, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange

from flaskapp import app


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_list=['test1','test2']
        if request.form['file'] in file_list:
            return 'sahi hai boss'
        else :
            flash ('galat value daala hai')
            return redirect(url_for('index'))

    else :
    	return render_template('index.html')