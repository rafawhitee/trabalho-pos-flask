import pandas as pd
import streamlit as st
import requests
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Any, List

base_url: str = f"http://localhost:5000/api"

st.title("Campeonato Brasileiro - Estatísticas")

def get_statistics() -> pd.DataFrame:
    response = requests.get(f"{base_url}/statistics")
    return pd.DataFrame(response.json()) if response and response.status_code == 200 else None

def get_partidas_by_team(time: str) -> List[dict]:
    response = requests.get(f"{base_url}/team/{time}")
    return response.json() if response and response.status_code == 200 else None

def get_partida_by_id(partida_id: int) -> dict:
    response = requests.get(f"{base_url}/record/{partida_id}")
    return response.json() if response and response.status_code == 200 else None

def generate_graphs_to_team(time: str, data: List[dict]) -> Any:
    cartoes: pd.DataFrame = create_year_col(pd.DataFrame(get_all_rows_by_dict_key(data, "cartoes", ["data_formatada"])))
    estatisticas: pd.DataFrame = create_year_col(pd.DataFrame(get_all_rows_by_dict_key(data, "estatisticas", ["data_formatada"])))
    gols: pd.DataFrame = create_year_col(pd.DataFrame(get_all_rows_by_dict_key(data, "gols", ["data_formatada"])))

    # Gráfico de Cartões Amarelos do Clube por Rodada
    plt.figure(figsize=(8, 6))
    sns.histplot(data=estatisticas[estatisticas["clube"].str.upper() == time.upper()], x='cartao_amarelo', 
                 hue="ano", palette='Set2', multiple="stack", discrete=True)
    st.pyplot(plt)

def create_year_col(df: pd.DataFrame) -> pd.DataFrame:
    df["data"] = pd.to_datetime(df["data_formatada"], format='%d/%m/%Y')
    df["ano"] = df['data'].dt.year.astype(str)
    return df

def get_all_rows_by_dict_key(data: List[dict], key: str, parent_fields: List[str] | None) -> List[dict]:
    rows = []
    for item in data:
        item_key_value = item[key]
        for item2 in item_key_value:
            if parent_fields != None and len(parent_fields) > 0:
                for parent_field in parent_fields:
                    item2[parent_field] = item[parent_field]
            rows.append(item2)
    return rows

st.write("Estatísticas Básicas")
st.dataframe(get_statistics())

partida_id_input = st.text_input("Consultar Partida pelo ID:")
if st.button(key="searchById", label="Pesquisar"):
    if partida_id_input:
        partida: dict = get_partida_by_id(partida_id_input)
        if partida != None:
            st.write(f"{partida["mandante"]} {partida["mandante_Placar"]} x {partida["visitante_Placar"]} {partida["visitante"]}")
            st.write(f"Data/Hora: {partida["data_formatada"]} {partida["hora"]}")
            st.write(f"Rodada: {partida["rodata"]}")
            st.write(f"Local: {partida["mandante_Estado"]}")
        else:
            st.error(f"Não foi encontrado a partida {partida_id_input}")
    else:
        st.error(f"Não foi encontrado a partida {partida_id_input}")


time_input = st.text_input("Visualizar Gráficos do Time:")
if st.button(key="searchByTeam", label="Pesquisar"):
    if time_input:
        partidas: List[dict] = get_partidas_by_team(time_input)
        if partidas != None and len(partidas) > 0:
            generate_graphs_to_team(time_input, partidas)
        else:
            st.error(f"Não foi encontrado nenhuma partida para o time {time_input}")
    else:
        st.error(f"Não foi encontrado nenhuma partida para o time {time_input}")