import pandas as pd

data = pd.read_csv("Mall_Customers.csv")

print(data.head())

X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

print("\nSelected Features:")
print(X.head())

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)

data['Cluster'] = kmeans.fit_predict(X)

print("\nClustered Data:")
print(data.head())

plt.figure(figsize=(8, 6))

plt.scatter(
    data['Annual Income (k$)'],
    data['Spending Score (1-100)'],
    c=data['Cluster']
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=200,
    marker='X'
)

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.show()

cluster_summary = data.groupby('Cluster')[
    ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
].mean()

print("\nCluster Summary:")
print(cluster_summary)

data.to_csv("Mall_Customers_Segmented.csv", index=False)

print("\nFinal segmented dataset saved successfully!")