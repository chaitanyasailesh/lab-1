import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
data_set = pd.read_csv('supermarkets.csv')
# encoding the categorical features
data_set = data_set.apply(LabelEncoder().fit_transform)
# EDA
print(data_set['Employees'].value_counts(dropna='False'))
# searching for attributes which have null values
nulls = pd.DataFrame(data_set.isnull().sum().sort_values(ascending=False))
nulls.columns = ['Null Count']
print(nulls)
numeric_features = data_set.select_dtypes(include=[np.number])
corr = numeric_features.corr()
# correlation of best features respected to target class
print(corr['Employees'].sort_values(ascending=False)[:4])
x = data_set.iloc[:, :]


# normalizing and preprocessing Data
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns=x.columns)

nclusters = 3
seed = 0

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)

# silhouette_score
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print('silhouette_score :', score)

wcss =[]
# elbow method
for i in range(1, 6):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 6), wcss)
plt.title('Elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()


# Plotting Clusters
LABEL_COLOR_MAP = {0 : 'red',
                   1 : 'black',
                   2 : 'cyan',
                   3 : 'green',
                   4 : 'gold',
                   5 : 'blue'


                   }
label_color = [LABEL_COLOR_MAP[l] for l in km.predict(X_scaled)]
plt.scatter(X_scaled_array[:, 0], X_scaled_array[:, 1], c=label_color)
plt.show()



