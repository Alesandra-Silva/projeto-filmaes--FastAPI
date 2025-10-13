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

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filme()
    lista = []
    for linha in filmes:
        lista.append({ 
            "id": linha[0],
            "título":linha[1],
            "genero": linha[2],
            "ano":linha[3],
            "avaliacao": linha[4]
            })
    return {"filmes": lista}