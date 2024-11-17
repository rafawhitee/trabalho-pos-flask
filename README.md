# Projeto de Estatítica com Streamlit - Campeonato Brasileiro Série A 2003-2023

# Requisitos
- Python 3.12 ou superior (https://www.python.org/downloads/release/python-3120/)

# Instalando o projeto
- Após instalar o Python na sua máquina
- Clone ou baixe o projeto (https://github.com/rafawhitee/trabalho-pos-flask/archive/refs/heads/main.zip)
- Abra um terminal e execute o seguinte comando para instalar as dependencias necessárias
```bash
pip install -r requirements.txt
```

# Executando o projeto
- Depois de instalar o Python e as dependências do projeto, vamos primeiramente subir a API
- No terminal, execute o seguinte comando para subir a API
```bash
python app/api.py
```
- Por padrão, ele irá subir um servidor de desenvolvimento na porta 5000, verifiue se a API subiu com sucesso: http://localhost:5000/api/record/7928
- Depois de subir a API, agora é hora de subir o Streamlit
- Aba um novo terminal (deixe o terminal com a API rodando, não feche-o) e execute o seguinte comando
```bash
streamlit run streamlit_app.py
```
- Por padrão, o Streamlit Run já abre uma aba do navegador padrão com a aplicação rodando (porta 8501), mas caso precise: http://localhost:8501

# Fluxo
1. Ao carregar o streamlit, a primeira tabela representa estatísticas básicas sobre as informações das partidas no geral, tais como cartões amarelo, escanteios, entre outros.
2. O primeiro um input que você digita o ID da partida e ele traz as informações da partida, como Mandante e Visitante e o placar do jogo e outras informações.
3. O segundo input você digita o nome do time desejado e ele traz 2 gráficos sobre a quantidade de gols que ele fez como Mandante e como Visitante.
4. O terceiro input aceita um csv para subir novos dados.