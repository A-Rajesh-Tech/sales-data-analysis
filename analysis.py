import pandas as pd

# Load data
df = pd.read_csv('data/sales_data.csv')

# Create total column
df['total'] = df['price'] * df['quantity']

print("\n📊 SALES DATA ANALYSIS REPORT")
print("="*40)

# Total Sales
total_sales = df['total'].sum()
print(f"\n💰 Total Sales: ₹{total_sales}")

# Sales by Region
print("\n🌍 Sales by Region:")
sales_by_region = df.groupby('region')['total'].sum()
for region, value in sales_by_region.items():
    print(f"   {region}: ₹{value}")

# Top Products
print("\n🛒 Top Products:")
sales_by_product = df.groupby('product')['total'].sum().sort_values(ascending=False)
for product, value in sales_by_product.items():
    print(f"   {product}: ₹{value}")

# Average Order Value
avg_order = df['total'].mean()
print(f"\n📈 Average Order Value: ₹{avg_order:.2f}")

print("\n" + "="*40)
print("✅ Analysis Completed")