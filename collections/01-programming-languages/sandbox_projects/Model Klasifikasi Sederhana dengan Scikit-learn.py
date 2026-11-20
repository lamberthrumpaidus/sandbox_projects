from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Mengambil dataset iris
iris = load_iris()
X = iris.data
y = iris.target

# Membagi data menjadi data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Membuat model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Memprediksi data uji
y_pred = model.predict(X_test)

# Mengevaluasi model
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
