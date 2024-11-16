# Projeto de Estatítica com Streamlit - Campeonato Brasileiro 2003-2023

# Requisitos
- Python 3.12

# Instalando o projeto
- Clone ou baixe o projeto
- Instale as dependencias necessárias
```bash
pip install -r requirements.txt
```

# Executando o projeto
- Primeiramente, vamos subir o Api com Flask, abra um novo terminal e execute
```bash
python app/api.py
```
- Por padrão, ele irá subir um servidor de desenvolvimento na porta 5000
- Para verificar se a API subiu com sucesso, abra uma aba do navegador com a seguinte URL http://localhost:5000/api/record/7928
- Depois de subir e verificar a API, agora é hora de subir o Streamlit
- Aba um novo terminal e execute o seguinte comando
```bash
streamlit run streamlit_app.py
```
- Por padrão, o streamlit já abre uma aba do navegador padrão com a aplicação rodando (porta 8501)