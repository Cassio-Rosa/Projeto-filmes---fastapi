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


def atualizar_filme(id, novo_titulo, novos_generos, novo_ano, nova_avalição ):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filmes SET titulo = %s,genero = %s, ano = %s, avaliacao = %s WHERE id = %s",
                  ( novo_titulo, novos_generos, novo_ano, nova_avalição, id)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atualizar a avaliação da tabela na tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()    

atualizar_filme(1, "rari poti 6 parte 9", "Magia, Poder", 2001, 6.9)