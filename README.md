# ⚡ Energy Consumption ML API

Esta é uma aplicação completa de Ciência de Dados e Engenharia, que utiliza Inteligência Artificial para prever o consumo de energia residencial com base em fatores climáticos e temporais.

# ⚡ Energy Consumption ML System

Este projeto é uma solução completa de Engenharia de Dados e Inteligência Artificial para prever o consumo de energia residencial. O sistema conta com um modelo de Machine Learning exposto via API e um Dashboard interativo para visualização dos resultados.

## 🔗 Links do Projeto (Online)
* **Dashboard Interativo:** [https://energy-ml-api-production.up.railway.app/](https://energy-ml-api-production.up.railway.app/)
* **API Documentation (Swagger):** [(https://web-production-31b64.up.railway.app/docs](https://web-production-31b64.up.railway.app/docs)

## 🏗️ Arquitetura do Sistema
O projeto foi dividido em dois serviços independentes hospedados no **Railway** (PaaS), seguindo boas práticas de separação de responsabilidades:

1.  **Back-end (API):** Desenvolvido com **FastAPI**, carrega o modelo de ML e processa as predições.
2.  **Front-end (Dashboard):** Desenvolvido com **Streamlit**, oferece uma interface amigável para simulação de dados e consulta à API.

## 🚀 Componentes Técnicos
* **Tratamento de Dados:** Limpeza, engenharia de features e análise exploratória realizadas em notebooks Python (`pandas`, `matplotlib`).
* **Modelo de ML:** Regressão treinada com `scikit-learn` (ajustado para as variáveis climáticas de Sobral/CE e base de dados original) e exportada via `joblib`.
* **Monitoramento:** Implementação de logs de observabilidade no Railway para rastreio de requisições em tempo real.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Bibliotecas de ML:** Scikit-Learn, NumPy, Pandas, Joblib.
* **Web & Interface:** FastAPI, Uvicorn, Streamlit, Requests.
* **Infraestrutura:** Git, GitHub, Railway (PaaS), Docker (implícito).

## 📊 Endpoints da API
A API recebe dados climáticos e temporais via método **POST** no endpoint `/predict`.

**Exemplo de Payload (JSON):**
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

5. Execute o Dashboard
   streamlit run dashboard.py