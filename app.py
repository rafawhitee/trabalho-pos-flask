import streamlit as st
import numpy as np

# Título do aplicativo
st.title("Calculadora Estatística Básica")

# Entrada de dados
st.write("Digite uma lista de números separados por vírgulas para calcular média, mediana e desvio padrão.")

# Entrada do usuário para uma lista de números
input_data = st.text_input("Números (ex: 1, 2, 3, 4, 5)")

# Processamento dos dados
if input_data:
    try:
        # Converte a entrada em uma lista de números
        numbers = np.array([float(num) for num in input_data.split(',')])
        
        # Calcula média, mediana e desvio padrão
        mean = np.mean(numbers)
        median = np.median(numbers)
        std_dev = np.std(numbers)
        
        # Exibe os resultados
        st.write("### Resultados Estatísticos")
        st.write(f"**Média:** {mean}")
        st.write(f"**Mediana:** {median}")
        st.write(f"**Desvio Padrão:** {std_dev}")
    except ValueError:
        st.error("Por favor, insira uma lista de números válidos separados por vírgulas.")