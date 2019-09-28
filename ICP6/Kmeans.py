import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")


dataset = pd.read_csv('CC.csv')




data = dataset.select_dtypes(include=[np.number]).interpolate().dropna()


# splitting the features and class
x = dataset
y = dataset.iloc[:,-1]


# see how many samples we have of each species
print(dataset["TENURE"].value_counts())

## Printing the count of Null values
nulls = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

## Replacing null values with mean values
x = x.select_dtypes(include=[np.number]).interpolate().dropna()

## Verifying Null values after replacing it with the mean value
nulls = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)


from sklearn.cluster import KMeans
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(x)



# Silhouette score represents how similar the data point in  cluster compared to the other clusters.
#  High value indicates that the object is well matched to its own cluster and poorly matched to neighboring clusters.


#  score with out scaling

y_cluster_kmeans = km.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print("With out Scaling : "+str(score))


# score with scaling


from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)


from sklearn.cluster import KMeans
nclusters=3
km=KMeans(n_clusters=nclusters)
km.fit(X_scaled)

y_scaled_Kmeans = km.predict(X_scaled)
from sklearn import metrics
score1 = metrics.silhouette_score(X_scaled,y_scaled_Kmeans)
print(" With Scaling: "+str(score1))



#      Elbow method


# ##elbow method to know the number of clusters
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()





#     PCA

# Reducing the dimensionality from 3 to 2 using PCA
pca = PCA(2)
x_pca = pca.fit_transform(X_scaled)
df2 = pd.DataFrame(data=x_pca)

# Building the model after Dimensionality redcution
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(df2)

# predict the cluster for each data point after applying PCA.
y_cluster_kmeans = km.predict(df2)
score = metrics.silhouette_score(df2, y_cluster_kmeans)
print("Silhoutte Score After PCA: " + str(score))