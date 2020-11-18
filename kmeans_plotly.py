from sklearn import datasets
from sklearn.cluster import KMeans
import json
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as pgo



# sepal length - 0
# sepal width - 1
# petal length - 2
# petal width - 3

def apply_kmeans_(X_var, Y_var, n_clusters):
    iris = datasets.load_iris()
    X = iris.data[:, [int(X_var), int(Y_var)]]
    k_means = KMeans(n_clusters=int(n_clusters), random_state=42)
    y_means = k_means.fit_predict(X)
    data =[]
    for i in range(int(n_clusters)):
        data.append(pgo.Scatter(x=X[y_means == i, 0], y=X[y_means == i, 1], mode ="markers"))
    data.append(pgo.Scatter(x=k_means.cluster_centers_[:, 0], y =k_means.cluster_centers_[:, 1], mode ="markers"))

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

