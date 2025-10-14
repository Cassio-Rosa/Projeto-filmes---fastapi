from fastapi import FastAPI
import funcao

#Rodar o fastapi:
#python -m uvicorn api:app --reload
#ENTRE NA PASTA

#Iniciar o fastapi
app = FastAPI(title="Gerenciador de filmes")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindos ao gerenciador de filmes"}

@app.post("/filmes")
def criar_filme(titulo:str, genero:str, ano:int, avaliacao: float):
    funcao.inserir_filmes(titulo, genero, ano, avaliacao)
    return { "mensagem": "Filme adicionado com sucesso!"}

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filme()
    lista = []
    for linha in filmes:
        lista.append({
            "ID": linha[0],
            "titulo": linha[1],
            "genero": linha[2],
            "ano": linha[3],
            "avaliacao": linha[4]
            })
    return {"filmes": lista}

@app.delete("/filmes")
def deletar_filmes(id: int):
    funcao.deletar_filme(id)
    return {"mensagem": "Filme Deletado com Sucesso"}

@app.put("/filmes/{id_filmes}")
def atualizar_filmes(id:int, novo_titulo:str, novos_generos:str, novo_ano:int, nova_avalição:float ):
    filme = funcao.buscar_filme(id)
    if filme:
        funcao.atualizar_filme(id, novo_titulo, novos_generos, novo_ano, nova_avalição )
        return {"mensagem":"Filme atualizado com sucesso!"}
    return {"error": "filme não encontrado"}