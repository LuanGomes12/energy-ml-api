# ==============================
# 1. Imports
# ==============================
from fastapi import FastAPI
import joblib
import numpy as np
import os

# ==============================
# 2. Inicializar API
# ==============================
app = FastAPI(
    title="Energy Consumption ML API",
    description="API para predição de consumo energético residencial",
    version="1.0"
)

# ==============================
# 3. Carregar modelo treinado
# ==============================
model = joblib.load("model/model.pkl")

# ==============================
# 4. Endpoint raiz
# ==============================
@app.get("/")
def home():
    return {"message": "Energy ML API is runing"}

# ==============================
# 5. Endpoint de predição
# ==============================
@app.post("/predict")
def predict(data: dict):
    """
    Recebe features em JSON e retorna consumo previsto.
    """

     # Converter dict → array
    features = np.array([list(data.values())])

    prediction = model.predict(features)

    return {
        "predicted_consumption": float(prediction[0])
    }

# Conectar com o Railway
if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=False
    )