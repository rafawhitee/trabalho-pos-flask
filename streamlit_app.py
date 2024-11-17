import pandas as pd
import streamlit as st
import requests
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Any, List

base_url: str = f"http://localhost:5000/api"

##
## MÉTODOS/FUNÇÕES
##

def get_statistics() -> pd.DataFrame:
    response = requests.get(f"{base_url}/statistics")
    return pd.DataFrame(response.json()) if response and response.status_code == 200 else None

def get_partidas_by_team(time: str) -> List[dict]:
    response = requests.get(f"{base_url}/team/{time}")
    return response.json() if response and response.status_code == 200 else None

def update_dataframe(file: Any) -> bool:
    response = requests.post(f"{base_url}/record/csv", files={"file": file})
    return True if response and response.status_code == 200 else False

def get_partida_by_id(partida_id: int) -> dict:
    response = requests.get(f"{base_url}/record/{partida_id}")
    return response.json() if response and response.status_code == 200 else None

def generate_graphs_to_team(time: str, data: List[dict]) -> Any:
    df = pd.DataFrame(data)
    df["data"] = pd.to_datetime(df["data"], format='%d/%m/%Y')
    df["ano"] = df['data'].dt.year.astype(str)
    df_mandante = df[df["mandante"].str.upper() == time.upper()]
    df_visitante = df[df["visitante"].str.upper() == time.upper()]

    gols_mandante_por_ano = df_mandante.groupby(["mandante", "ano"])["mandante_Placar"].sum().reset_index()
    plt.figure(figsize=(8, 6))
    plt.title(f'Gols Feitos {time} (mandante) por Ano')
    ax_gols_mandante = sns.barplot(data=gols_mandante_por_ano, x='mandante', y="mandante_Placar", hue="ano", palette="Set2")
    add_specify_number_on_histplot(ax_gols_mandante)
    st.pyplot(plt)

    gols_visitante_por_ano = df_visitante.groupby(["visitante", "ano"])["visitante_Placar"].sum().reset_index()
    plt.figure(figsize=(8, 6))
    plt.title(f'Gols Feitos {time} (mandante) por Ano')
    ax_gols_visitante = sns.barplot(data=gols_visitante_por_ano, x='visitante', y="visitante_Placar", hue="ano", palette="Set2")
    add_specify_number_on_histplot(ax_gols_visitante)
    st.pyplot(plt)

def add_specify_number_on_histplot(ax):
    for patch in ax.patches:
        height = patch.get_height()  
        if height > 0: 
            x = patch.get_x() + patch.get_width() / 2
            ax.text(x, height + 0.5, f'{int(height)}', ha='center', fontsize=10, color='black')

def get_all_rows_by_dict_key(data: List[dict], key: str, parent_fields: List[str] | None = None) -> List[dict]:
    rows = []
    for item in data:
        item_key_value = item[key]
        for item2 in item_key_value:
            if parent_fields != None and len(parent_fields) > 0:
                for parent_field in parent_fields:
                    item2[parent_field] = item[parent_field]
            rows.append(item2)
    return rows

##
## STREAMLIT
##

st.title("Campeonato Brasileiro Série A - Estatísticas")

st.write("Estatísticas Básicas")
st.dataframe(get_statistics())

partida_id_input = st.text_input("Consultar Partida pelo ID:")
if st.button(key="searchById", label="Pesquisar"):
    try:
        if partida_id_input:
            partida: dict = get_partida_by_id(partida_id_input)
            if partida != None:
                st.write(f"{partida["mandante"]} {partida["mandante_Placar"]} x {partida["visitante_Placar"]} {partida["visitante"]}")
                st.write(f"Data/Hora: {partida["data"]} {partida["hora"]}")
                st.write(f"Rodada: {partida["rodata"]}")
                st.write(f"Local: {partida["mandante_Estado"]}")
            else:
                st.error(f"Não foi encontrado a partida {partida_id_input}")
        else:
            st.error(f"Não foi encontrado a partida {partida_id_input}")
    except:
        st.error(f"Não foi encontrado a partida {partida_id_input}")

time_input = st.text_input("Visualizar Gráficos do Time:")
if st.button(key="searchByTeam", label="Pesquisar"):
    try:
        if time_input:
            partidas: List[dict] = get_partidas_by_team(time_input)
            if partidas != None and len(partidas) > 0:
                generate_graphs_to_team(time_input, partidas)
            else:
                st.error(f"Não foi encontrado nenhuma partida para o time {time_input}")
        else:
            st.error(f"Não foi encontrado nenhuma partida para o time {time_input}")
    except:
        st.error(f"Ocorreu um erro ao montar os gráficos do time {time_input}")


uploaded_file = st.file_uploader("Inserir Novos Dados (Arquivo CSV)", type=["csv"])
if uploaded_file:
    try:
        sucesso: bool = update_dataframe(uploaded_file)
        if sucesso:
            st.success("Dados atualizados com sucesso!")
        else:
            st.error(f"Ocorreu um erro ao atualizar o dataframe")
    except:
        st.error(f"Ocorreu um erro ao atualizar o dataframe")