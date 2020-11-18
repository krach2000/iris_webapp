from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import io


# sepal length - 0
# sepal width - 1
# petal length - 2
# petal width - 3

def apply_kmeans(X_var, Y_var, n_clusters):
    iris = datasets.load_iris()
    X = iris.data[:, [int(X_var), int(Y_var)]]
    k_means = KMeans(n_clusters=int(n_clusters), random_state=42)
    y_means = k_means.fit_predict(X)
    plt.clf()
    for i in range(int(n_clusters)):
        plt.scatter(X[y_means == i, 0], X[y_means == i, 1], s=100)
    plt.scatter(k_means.cluster_centers_[:, 0], k_means.cluster_centers_[:, 1], s=200)
    plt.title('K-means using Iris')
    plt.xlabel(iris.feature_names[X_var])
    plt.ylabel(iris.feature_names[Y_var])

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    buffer = b''.join(buf)
    b2 = base64.b64encode(buffer)
    graph = b2.decode('utf-8')
    return graph

