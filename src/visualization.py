import matplotlib.pyplot as plt
import seaborn as sns

def sales_visualization(df):

    # Sales by Category
    plt.figure(figsize=(8,5))
    sns.barplot(x='Category', y='Sales', data=df)
    plt.title("Sales by Category")
    plt.xticks(rotation=45)
    plt.savefig('images/top_products.png')
    plt.show()

    # Monthly Sales Trend
    monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

    plt.figure(figsize=(10,5))
    monthly_sales.plot(kind='line', marker='o')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.savefig('images/sales_trend.png')
    plt.show()
