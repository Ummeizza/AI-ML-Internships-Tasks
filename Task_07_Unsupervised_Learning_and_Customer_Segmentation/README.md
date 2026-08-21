# Task 07 — Unsupervised Learning and Customer Segmentation

## 📌 Overview

This project applies unsupervised learning techniques to segment customers based on demographic and spending behavior.

The Mall Customer Segmentation dataset was used to identify meaningful customer groups that can support targeted marketing campaigns.

## 🎯 Objectives

- Understand unsupervised learning and customer segmentation
- Apply multiple clustering algorithms
- Determine an appropriate number of customer segments
- Compare clustering performance using evaluation metrics
- Visualize clusters using PCA
- Profile and interpret customer segments
- Translate clustering results into business recommendations

## 📊 Dataset

**Dataset:** Mall Customer Segmentation

**Source:** Kaggle

The dataset contains 200 customers with information including:

- Customer ID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

The clustering analysis used:

- Age
- Annual Income (k$)
- Spending Score (1-100)

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## 🔬 Methodology

The project follows these main steps:

1. Data loading and inspection
2. Data cleaning and preprocessing
3. Feature selection
4. Feature standardization
5. K-Means clustering
6. Elbow Method analysis
7. Silhouette analysis
8. DBSCAN clustering
9. Agglomerative Hierarchical Clustering
10. Algorithm comparison
11. PCA visualization
12. Customer cluster profiling
13. Business interpretation

## 📈 Results

| Algorithm | Clusters | Silhouette Score |
|-----------|----------|------------------|
| K-Means | 6 | 0.4284 |
| DBSCAN | Variable | 0.5190 |
| Hierarchical Clustering | 6 | 0.4201 |

DBSCAN achieved the highest Silhouette Score, but classified 98 of the 200 customers as noise.

Therefore, **K-Means with six clusters** was selected as the final business solution because it assigns every customer to a segment and satisfies the requirement of creating 4–6 marketing personas.

## 👥 Business Insights

The identified customer segments can support targeted marketing strategies such as:

- Premium offers for high-value customers
- Personalized campaigns for high-income but low-spending customers
- Engagement campaigns for high-spending customers
- Value-oriented promotions for lower-income customers
- Loyalty incentives for moderate-spending customers

