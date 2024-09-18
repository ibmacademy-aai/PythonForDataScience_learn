# pengelompokan dataframe data
import pandas as pd

# DataFrame dengan data penjualan
data = {
    'sales': ['Arifian', 'Cindy', 'Fariq', 'Belgis', 'Tiwi', 'Omi'],
    'asalkota': ['Tanjunguban', 'Tanjungpinang', 'Tanjunguban', 'Batam', 'Batam', 'Tanjungpinang'],
    'penjualan': [22000, 30000, 45000, 21000, 89000, 12000]
}
df = pd.DataFrame(data)

# Group by berdasarkan asal kota dan hitung total penjualan
grouped_sales = df.groupby('asalkota')['penjualan'].sum()

print(grouped_sales)