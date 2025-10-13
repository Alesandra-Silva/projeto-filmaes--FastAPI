from fastapi import FastAPI
import funcao

#Rodar o fastapi 
# python -m uvicorn api:app --reload

# /docs > Documentação Swagger
# /redoc > Documentação redoc

#Iniciar o fastapi
app = FastAPI(title= "Gerenciador de filmes")


@app.get("/")
def home():
    return {"mensagem":"Quero café prof"}

@app.post("/filmes")
def cria_filmes(título: str, genero: str, ano: int, avaliacao: float):
    funcao.inserir_filmes(título, genero, ano, avaliacao)
    return { "mensagem": "Filme adicionado com sucesso!"}