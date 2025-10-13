import streamlit as st
import requests

#URL da API FatAPI
API_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="Gerenciador de Filmes", page_icon="🎬")
st.title("🎥 Gerenciador de filmes")

menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar filme"])
if menu == "Catalogo":
    st.subheader("Todos os filmes disponíveis!")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(f"**{filme['título']}**")
    else:
        st.error("Erro ao acessar a API")