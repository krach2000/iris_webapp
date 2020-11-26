from flask import Flask, render_template, request, jsonify
from kmeans_plotly import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/cluster_num', methods=['GET', 'POST'])
def cluster_num():
    x_var = int(request.json["x_var"])
    y_var = int(request.json["y_var"])
    cluster_num = int(request.json["cluster_num"])
    data = apply_kmeans_(x_var, y_var, cluster_num)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
