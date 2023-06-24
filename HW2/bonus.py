from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()

k_values = list(range(1, 11))
inertias = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=0)
    kmeans.fit(iris.data)
    
    inertias.append(kmeans.inertia_)

diff_inertias = np.diff(inertias)

diff2_inertias = np.diff(diff_inertias)

elbow_index = np.argmax(diff2_inertias) + 1 

plt.figure(figsize=(10,6))
plt.plot(k_values, inertias, '-o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.xticks(k_values)

plt.annotate('Elbow at k=%d' % (elbow_index+1), xy=(elbow_index+1, inertias[elbow_index]), xytext=(elbow_index+1, inertias[elbow_index]+30), arrowprops=dict(facecolor='black', shrink=0.05))

plt.savefig('elbow.png')
