# Task 07 — Unsupervised Learning and Customer Segmentation

## 1. Overview

This task focuses on applying unsupervised learning techniques to segment customers based on their demographic and spending behavior. The Mall Customer Segmentation dataset was used to identify meaningful customer groups that can support targeted marketing strategies.

The main algorithms evaluated were K-Means, DBSCAN, and Agglomerative Hierarchical Clustering.

## 2. Dataset

The Mall Customer Segmentation dataset contains 200 customer records with the following attributes:

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

For clustering, the following numerical features were selected:

- Age
- Annual Income (k$)
- Spending Score (1-100)

CustomerID was excluded because it is an identifier rather than a meaningful behavioral feature. Gender was also not used in the clustering model.

## 3. Data Preprocessing

The dataset was inspected for missing values, duplicate records, and data types.

The selected numerical features were standardized using `StandardScaler` before applying the clustering algorithms. Standardization was necessary because the features have different numerical ranges and scales.

No target variable was used because this is an unsupervised learning problem.

## 4. Clustering Methodology

Three clustering algorithms were evaluated:

### K-Means

K-Means was tested with different numbers of clusters using the Elbow Method and Silhouette Analysis. Six clusters were selected as the final solution because they provide a suitable balance between cluster separation and the business requirement of creating 4–6 customer personas.

### DBSCAN

DBSCAN was evaluated using density-based clustering. It achieved a higher Silhouette Score than K-Means, but classified a large number of customers as noise, making it less suitable for complete customer segmentation.

### Agglomerative Hierarchical Clustering

Agglomerative Hierarchical Clustering was also tested with six clusters. Its performance was comparable to K-Means and provided another useful clustering perspective.

## 5. Model Evaluation

The clustering algorithms were compared using Silhouette Score.

| Algorithm | Number of Clusters | Silhouette Score |
|-----------|--------------------|------------------|
| K-Means | 6 | 0.4284 |
| DBSCAN | Variable | 0.5190 |
| Hierarchical Clustering | 6 | 0.4201 |

Although DBSCAN achieved the highest Silhouette Score of 0.5190, it classified 98 out of 200 customers as noise. Therefore, K-Means was selected as the final business solution because it assigns every customer to a defined segment and satisfies the requirement of creating 4–6 marketing personas.

## 6. PCA Visualization

Principal Component Analysis (PCA) was used to reduce the standardized feature space to two dimensions for visualization.

The PCA visualization provided a two-dimensional representation of the customer clusters and helped assess the separation between the identified customer groups.

## 7. Customer Segmentation

The final K-Means model produced six customer segments based on age, annual income, and spending behavior.

The clusters represent different customer profiles, including high-value customers, high-income customers with lower spending behavior, and lower-income customers with varying spending patterns.

These segments can be used to design differentiated marketing strategies instead of applying the same campaign to every customer.

## 8. Business Interpretation

The identified customer segments can support targeted marketing decisions.

- High-income and high-spending customers can be targeted with premium offers and loyalty programs.
- High-income but lower-spending customers can receive personalized offers designed to increase engagement.
- Younger high-spending customers can be targeted with trend-focused promotions.
- Lower-income customers can receive value-oriented discounts and affordable product recommendations.
- Moderate-spending customers can be encouraged through personalized promotions and loyalty incentives.

## 9. Limitations

- The dataset contains only 200 customers, while the business scenario describes approximately 200K customers.
- Only age, annual income, and spending score were used for segmentation.
- K-Means requires the number of clusters to be selected in advance.
- DBSCAN was sensitive to its parameters and classified a large proportion of observations as noise.
- The identified customer personas should be validated using a larger and more representative dataset before real-world deployment.

## 10. Conclusion

The analysis demonstrated how unsupervised learning can be used for customer segmentation. K-Means, DBSCAN, and Agglomerative Hierarchical Clustering were implemented and compared.

DBSCAN achieved the highest numerical Silhouette Score, but its large number of noise points reduced its usefulness for assigning every customer to a marketing persona. K-Means with six clusters was therefore selected as the final approach.

The resulting customer segments provide a practical foundation for personalized marketing campaigns and demonstrate how clustering can transform customer behavior data into actionable business insights.