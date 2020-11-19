from flask import Flask, render_template, session, redirect, url_for, session, send_file, request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextField,
                     TextAreaField, SubmitField)
from wtforms.validators import DataRequired
from kmeans import *
from kmeans_plotly import *
import numpy as np
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


class inputForm(FlaskForm):
    x_var = SelectField('Please choose X-variable: ',
                        choices=[('0', 'Sepal Width'), ('1', 'Sepal Length'), ('2', 'Petal Width'),
                                 ('3', 'Petal Length')])
    y_var = SelectField('Please choose Y-variable: ',
                        choices=[('0', 'Sepal Width'), ('1', 'Sepal Length'), ('2', 'Petal Width'),
                                 ('3', 'Petal Length')])
    cluster_num = SelectField('Please choose number of clusters:',
                              choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = inputForm()
    graphJSON= None
    graph = None

    if form.validate_on_submit():
        session['x_var'] = form.x_var.data
        session['y_var'] = form.y_var.data
        session['cluster_num'] = form.cluster_num.data
        graph = apply_kmeans(int(session['x_var']), int(session['y_var']), int(session['cluster_num']))

        graphJSON = apply_kmeans_(int(session['x_var']), int(session['y_var']), int(session['cluster_num']))

        return render_template('index.html', form=form, graph=graph,graphJSON=graphJSON)

    return render_template('index.html', form=form, graph=None,graphJSON=None)




if __name__ == '__main__':
    app.run(debug=True)
