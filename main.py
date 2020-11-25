from flask import Flask, render_template, session, redirect, url_for, session, send_file, request, jsonify
from kmeans import *
from kmeans_plotly import *
import numpy as np
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'



@app.route('/', methods=['GET', 'POST'])
def index():

    #if request.method == "POST":
        #x_var = request.form['x_var']
        #y_var = request.form['y_var']
        #cluster_num = request.form.get('cluster_num')
        # graph = apply_kmeans(int(session['x_var']), int(session['y_var']), int(session['cluster_num']))

        #graphJSON = apply_kmeans_(int(x_var), int(y_var), int(cluster_num))

        #return render_template('index.html', graph=None, graphJSON=graphJSON)

    return render_template('index.html', graph=None, graphJSON=None)


@app.route('/cluster_num', methods=['GET', 'POST'])
def cluster_num():
    print(request.json["cluster_num"])
    x_var = 1
    y_var = 2
    cluster_num = int(request.json["cluster_num"])
    data = apply_kmeans_(x_var, y_var, cluster_num)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
