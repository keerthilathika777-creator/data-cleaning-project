import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/Online Retail.csv", nrows=1000)

sns.heatmap(df.isnull(), cbar=False)
plt.show()

sns.boxplot(x=df['UnitPrice'])
plt.show()

df = df.dropna()

df = df.drop_duplicates()

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df = df[df['Quantity'] > 0]

df = df[df['UnitPrice'] > 0]

df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

df['Year'] = df['InvoiceDate'].dt.year

df['Month'] = df['InvoiceDate'].dt.month

df.to_csv("../cleaned_data/cleaned_retail_data.csv", index=False)

print("Data Cleaning Completed Successfully")
