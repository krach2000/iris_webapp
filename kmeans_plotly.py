from sklearn import datasets
from sklearn.cluster import KMeans

# sepal length - 0
# sepal width - 1
# petal length - 2
# petal width - 3

def apply_kmeans_(X_var, Y_var, n_clusters):
    iris = datasets.load_iris()
    X = iris.data[:, [int(X_var), int(Y_var)]]
    k_means = KMeans(n_clusters=int(n_clusters), random_state=42)
    y_means = k_means.fit_predict(X)
    data = {}

    for i in range(int(n_clusters)):
        x_name = "XT" + str(i)
        y_name = "YT" + str(i)
        data[x_name] = X[y_means == i, 0].tolist()
        data[y_name] = X[y_means == i, 1].tolist()
    x_name = "XCC"
    y_name = "YCC"
    data[x_name] = k_means.cluster_centers_[:, 0].tolist()
    data[y_name] = k_means.cluster_centers_[:, 1].tolist()
    return data
