from conexao import conectar
#pip install psycopg2 dotenv streamlit fastapi uvicorn requests

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS filmes(
                           
                id SERIAL PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INTEGER NOT NULL,
                avaliacao REAL
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()



def inserir_filmes(titulo, genero, ano, avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filme na tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()


def listar_filme():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM filmes ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao tentar listar os filmes na tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()    
