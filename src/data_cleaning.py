import pandas as pd

def clean_data():
    df = pd.read_csv('data/retail_sales.csv')

    # Remove missing values
    df.dropna(inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert date column
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    print("Data cleaned successfully!")
    return df
