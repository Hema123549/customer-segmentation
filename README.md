# Customer Segmentation using K-Means Clustering

## 📌 Project Overview

This project performs customer segmentation using the K-Means clustering algorithm. Customers are grouped based on their annual income and spending score to identify different customer behavior patterns.

## 🎯 Objective

The main objective of this project is to:

- Segment customers into different groups
- Analyze customer spending behavior
- Identify high-spending and low-spending customer groups
- Generate useful business insights from customer data

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- K-Means Clustering

## 📊 Dataset

The dataset contains customer information such as:

- Customer ID
- Gender
- Age
- Annual Income
- Spending Score

For clustering, the following two features were selected:

- Annual Income (k$)
- Spending Score (1-100)

## 🔍 Methodology

1. Loaded the customer dataset using Pandas
2. Selected relevant features for clustering
3. Used the Elbow Method to determine the number of clusters
4. Applied K-Means clustering
5. Visualized the customer segments
6. Calculated the average values for each cluster
7. Saved the segmented dataset as a CSV file

## 📈 Customer Segments

The analysis identified five customer segments:

| Cluster | Customer Segment |
|---|---|
| 0 | Moderate Income & Moderate Spending |
| 1 | High Income & High Spending |
| 2 | Low Income & High Spending |
| 3 | High Income & Low Spending |
| 4 | Low Income & Low Spending |

## 💡 Key Insights

- Cluster 1 represents customers with high income and high spending.
- Cluster 2 represents customers with relatively low income but high spending.
- Cluster 3 represents customers with high income but low spending.
- Cluster 4 represents customers with low income and low spending.
- Cluster 0 represents customers with moderate income and spending.

## 🏁 Conclusion

K-Means clustering successfully divided customers into five distinct groups based on income and spending behavior. These segments can help businesses understand their customers and design targeted marketing strategies.

## 👩‍💻 Author

Hema M
