import pandas as pd

# Membaca file CSV
data = pd.read_csv('data.csv')

# Menampilkan data pertama
print(data.head())

# Menghitung rata-rata dari kolom tertentu
average = data['column_name'].mean()
print(f'Rata-rata kolom: {average}')

# Menyimpan data hasil perubahan ke file baru
data.to_csv('data_processed.csv', index=False)
