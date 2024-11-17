import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]
data = np.random.normal(size=1000)

# 1. Line Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Sine Wave', color='blue')
plt.plot(x, y2, label='Cosine Wave', color='orange')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()

# 2. Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='green')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 3. Histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Sine Points')
plt.scatter(x, y2, color='blue', label='Cosine Points')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

# 5. Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# 6. Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=[data, data + 1, data - 1], palette='Set3')
plt.title('Box Plot')
plt.xticks([0, 1, 2], ['Dataset 1', 'Dataset 2', 'Dataset 3'])
plt.show()

# 7. Area Plot
plt.figure(figsize=(10, 6))
plt.fill_between(x, y, color='skyblue', alpha=0.5)
plt.fill_between(x, y2, color='orange', alpha=0.5)
plt.title('Area Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 8. Heatmap
matrix_data = np.random.rand(10, 12)
plt.figure(figsize=(10, 6))
sns.heatmap(matrix_data, annot=True, fmt=".1f", cmap='coolwarm')
plt.title('Heatmap')
plt.show()