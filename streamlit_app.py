import pandas as pd
import streamlit as st
import requests

base_url: str = f"http://localhost:5000/api"

st.title("Campeonato Brasileiro - Estatísticas")

def get_statistics() -> pd.DataFrame:
    response = requests.get(f"{base_url}/statistics")
    return pd.DataFrame(response.json()) if response and response.status_code == 200 else None

def get_partida_info(partida_id: int) -> dict:
    response = requests.get(f"{base_url}/record/{partida_id}")
    return response.json() if response and response.status_code == 200 else None

st.write("Estatísticas Básicas")
st.dataframe(get_statistics())

st.write("Consultar Partida pelo ID")
partida_id_input = st.text_input("Digite o ID:")

if st.button("Pesquisar"):
    if partida_id_input:
        df: dict = get_partida_info(partida_id_input)
        if df is not None:
            st.table(df)
    else:
        st.error(f"Não foi encontrado a partida {partida_id_input}")