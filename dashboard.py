import streamlit as st
import requests

# Configuração visual
st.set_page_config(page_title="Energy Intelligence", page_icon="💡")

st.title("💡 Energy Consumption Dashboard")
st.markdown("Interface interativa para predição de consumo energético via API no Railway.")

# Criando colunas para o layout ficar organizado
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌐 Ambiente Externo")
    t_out = st.number_input("Temperatura Externa (T_out)", value=5.2)
    press = st.number_input("Pressão (Press_mm_hg)", value=760.0)
    rh_out = st.slider("Umidade Externa (RH_out)", 0, 100, 80)
    wind = st.number_input("Vento (Windspeed)", value=3.5)
    vis = st.number_input("Visibilidade", value=40.0)
    tdew = st.number_input("Ponto de Orvalho (Tdewpoint)", value=2.1)

with col2:
    st.subheader("🏠 Ambiente Interno e Tempo")
    lights = st.number_input("Luzes (lights)", value=10)
    avg_temp = st.number_input("Média Temp Interna", value=19.5)
    avg_hum = st.number_input("Média Umid Interna", value=45.2)
    
    st.divider()
    hour = st.slider("Hora do Dia", 0, 23, 18)
    month = st.selectbox("Mês", list(range(1, 13)), index=0)
    day_of_week = st.sidebar.selectbox("Dia da Semana (0=Seg, 6=Dom)", list(range(7)), index=2)
    is_weekend = st.sidebar.radio("É Final de Semana?", [0, 1], index=0)

# Botão de ação
if st.button("🚀 Calcular Previsão de Consumo"):
    # Monte o dicionário exatamente como a API espera
    payload = {
        "lights": lights,
        "T_out": t_out,
        "Press_mm_hg": press,
        "RH_out": rh_out,
        "Windspeed": wind,
        "Visibility": vis,
        "Tdewpoint": tdew,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend,
        "month": month,
        "avg_temp": avg_temp,
        "avg_humidity": avg_hum
    }

    # URL da sua API no Railway (substitua pela sua real)
    URL_RAILWAY = "https://web-production-31b64.up.railway.app/predict"

    with st.spinner('Consultando a inteligência da API...'):
        try:
            response = requests.post(URL_RAILWAY, json=payload)
            if response.status_code == 200:
                resultado = response.json()
                consumo = resultado["predicted_consumption"]
                st.metric(label="Consumo Previsto", value=f"{consumo:.2f} Wh")
                st.balloons() # Um toque de comemoração!
            else:
                st.error(f"Erro na API: {response.status_code}")
                st.write(response.text)
        except Exception as e:
            st.error(f"Não foi possível conectar: {e}")