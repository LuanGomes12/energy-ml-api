# Imports
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Carregar a base de dados tratada
df = pd.read_csv("data/KAG_energydata_processed.csv")

print("Base carregada:", df.shape)

# Separar features(X) e targets (y)
X = df.drop(columns=["Appliances"])
y = df["Appliances"]

print("\nX Shape:", X.shape)
print("Y Shape:", y.shape)

# Divisão em dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTreino:", X_train.shape)
print("Teste:", X_test.shape)

# Criação do modelo
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Treinamento do modelo
model.fit(X_train, y_train)
print("\nModelo treinado.")

# Avaliação do modelo
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMAE: {mae:.2f}")
print(f"R2: {r2:.4f}")

# Salvar modelo
joblib.dump(model, "model/model.pkl")

print("\nModelo salvo em model/model.pkl")