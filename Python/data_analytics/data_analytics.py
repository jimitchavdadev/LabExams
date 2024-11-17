import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Data Loading
data = pd.read_excel('Online Retail.xlsx')

# Step 2: Data Cleaning
print("Missing values in each column:")
print(data.isnull().sum())

data.dropna(subset=['CustomerID', 'InvoiceDate'], inplace=True)
data.drop_duplicates(inplace=True)
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]
data['TotalAmountSpent'] = data['Quantity'] * data['UnitPrice']

# Customer summary
customer_summary = data.groupby('CustomerID').agg(
    TotalAmountSpent=('TotalAmountSpent', 'sum'),
    TotalItemsPurchased=('Quantity', 'sum'),
    LastPurchaseDate=('InvoiceDate', 'max')
).reset_index()

customer_summary['AveragePurchaseValue'] = (
    customer_summary['TotalAmountSpent'] / customer_summary['TotalItemsPurchased']
)

# Step 3: Descriptive Statistics
print("\nDescriptive Statistics:")
print(customer_summary.describe())

# Step 4: Customer Segmentation using KMeans
scaler = StandardScaler()
X = scaler.fit_transform(customer_summary[['TotalAmountSpent', 'TotalItemsPurchased', 'AveragePurchaseValue']])

inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
customer_summary['Segment'] = kmeans.fit_predict(X)

# Step 5: Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=customer_summary, x='TotalAmountSpent', y='TotalItemsPurchased', 
    hue='Segment', palette='viridis', size='AveragePurchaseValue', sizes=(50, 500)
)
plt.title('Customer Segmentation')
plt.xlabel('Total Amount Spent')
plt.ylabel('Total Items Purchased')
plt.legend(title='Segment')
plt.show()

# Step 6: Customer Insights
segment_summary = customer_summary.groupby('Segment').agg(
    TotalAmountSpent=('TotalAmountSpent', 'mean'),
    TotalItemsPurchased=('TotalItemsPurchased', 'mean'),
    AveragePurchaseValue=('AveragePurchaseValue', 'mean'),
    LastPurchaseDate=('LastPurchaseDate', 'max')
).reset_index()

print("\nCustomer Segment Insights:")
print(segment_summary)

# Step 7: Customer Engagement Recommendations
recommendations = {
    0: "High Spenders: Offer exclusive deals and loyalty programs to retain their business.",
    1: "Frequent Shoppers: Provide personalized recommendations and discounts on their favorite items.",
    2: "Inactive Customers: Send re-engagement emails with special offers to encourage them to return."
}

print("\nCustomer Engagement Recommendations:")
for segment, recommendation in recommendations.items():
    print(f"Segment {segment}: {recommendation}")
