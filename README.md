# ⚡ Energy Consumption ML API

Esta é uma aplicação completa de Ciência de Dados e Engenharia, que utiliza Inteligência Artificial para prever o consumo de energia residencial com base em fatores climáticos e temporais.

## 🚀 Estrutura do Projeto

* **Tratamento de Dados:** Limpeza e análise exploratória realizadas em notebooks Python (`pandas`, `matplotlib`).
* **Modelo de ML:** Regressão treinada com `scikit-learn` e salva em formato `.pkl` via `joblib`.
* **API:** Interface de comunicação desenvolvida com **FastAPI**.
* **Nuvem:** Hospedagem e deploy contínuo realizados no **Railway**.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Bibliotecas de ML:** Scikit-Learn, NumPy, Pandas, Joblib.
* **Framework Web:** FastAPI, Uvicorn (Servidor ASGI).
* **Infraestrutura:** Git, GitHub, Railway (PaaS).

## 📊 Como a API funciona?

A API expõe um endpoint principal:
* `POST /predict`: Recebe um JSON com variáveis climáticas (Temperatura, Humidade, Velocidade do Vento, etc.) e retorna a previsão de consumo energético em tempo real.

**Exemplo de entrada (JSON):**
```json
{
  "lights": 10,
  "T_out": 5.2,
  "Press_mm_hg": 760,
  "RH_out": 80,
  "Windspeed": 3.5,
  "Visibility": 40,
  "Tdewpoint": 2.1,
  "hour": 18,
  "day_of_week": 2,
  "is_weekend": 0,
  "month": 1,
  "avg_temp": 19.5,
  "avg_humidity": 45.2
}
```

## 🔧 Como rodar localmente

1. Clone o repositório:
   git clone https://github.com/seu-usuario/energy-ml-api.git

2. Crie e ative o ambiente virtual:
   python -m venv venv
   .\venv\Scripts\activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Inicie o servidor:
   uvicorn app:app --reload