from sklearn.linear_model import LinearRegression
import numpy as np

# Data contoh: Ukuran rumah dan harga
# Ukuran rumah dalam kaki persegi
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([200000, 250000, 300000, 350000, 400000])  # Harga rumah

# Membuat model regresi linier
model = LinearRegression()
model.fit(X, y)

# Prediksi harga untuk rumah dengan ukuran 2200 kaki persegi
predicted_price = model.predict([[2200]])
print(f'Prediksi harga rumah 2200 sq ft: ${predicted_price[0]:,.2f}')
