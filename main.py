import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/supermarket_sales.csv')  

# Preview
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Add Month column
df['Month'] = pd.to_datetime(df['Date']).dt.month

# Monthly sales
monthly_sales = df.groupby('Month')['Total'].sum()
plt.figure(figsize=(10, 5))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# Top 10 Selling Products by Revenue
top_products = df.groupby('Product line')['Total'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Selling Products by Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Product Description")
plt.show()

# Sales by Branch
country_sales = df.groupby('Branch')['Total'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=country_sales.values, y=country_sales.index)
plt.title("Top Countries by Total Sales")
plt.xlabel("Total Revenue")
plt.ylabel("Branch")
plt.show()

# Distribution of Invoice Value
invoice_value = df.groupby('Invoice ID')['Total'].sum()
plt.figure(figsize=(10, 5))
sns.histplot(invoice_value, bins=50, kde=True)
plt.title("Distribution of Invoice Total Value")
plt.xlabel("Invoice Value")
plt.ylabel("Number of Invoices")
plt.show()

# Profit Analysis by Product Line
product_profit = df.groupby('Product line').agg({
    'Quantity': 'sum',
    'Total': 'sum',
    'gross income': 'sum',
    'gross margin percentage': 'mean'
}).sort_values(by='Total', ascending=False)

# Plot Total Revenue by Product Line
plt.figure(figsize=(12, 6))
sns.barplot(x=product_profit['Total'], y=product_profit.index)
plt.title("Total Revenue by Product Line")
plt.xlabel("Total Revenue")
plt.ylabel("Product Line")
plt.show()

# Plot Gross Income by Product Line
plt.figure(figsize=(12, 6))
sns.barplot(x=product_profit['gross income'], y=product_profit.index)
plt.title("Gross Income by Product Line")
plt.xlabel("Gross Income")
plt.ylabel("Product Line")
plt.show()


