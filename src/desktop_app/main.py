import pyodbc

from datetime import date

from desktop_app.models.livro import Livro
from desktop_app.dao.livro_dao import LivroDAO
import desktop_app.dao.database as database
import desktop_app.utils.tools as tools

def test_db_connection():
    """
    Tests the database connection by attempting to connect and printing the result.
    """
    myDao = database.DAO()
    print(myDao)
    connection = myDao.connect()

    if connection:
        print("Test DB Connection: Success")
        myDao.__del__()
    else:
        print("Test DB Connection: Failed")

def print_table(rows, headers, max_width=40):
    # converte tudo para string (com truncagem)
    def fmt(v):
        s = "" if v is None else str(v)
        s = s.replace("\n", " ")
        return (s[: max_width - 1] + "…") if len(s) > max_width else s

    data = [[fmt(v) for v in row] for row in rows]
    cols = list(zip(*([headers] + data))) if headers else list(zip(*data))

    widths = [max(len(x) for x in col) for col in cols]

    # header
    line = " | ".join(h.ljust(w) for h, w in zip(headers, widths))
    sep  = "-+-".join("-" * w for w in widths)
    print(line)
    print(sep)

    # rows
    for row in data:
        print(" | ".join(cell.ljust(w) for cell, w in zip(row, widths)))        

def list_table(conn: pyodbc.Connection, table: str, schema: str = "dbo", top: int = 100):
    # validação simples para evitar SQL injection em nomes
    import re
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", table) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", schema):
        raise ValueError("Invalid schema/table name")

    sql = f"SELECT TOP ({top}) * FROM [{schema}].[{table}];"

    cur = conn.cursor()
    cur.execute(sql)

    headers = [c[0] for c in cur.description]
    rows = cur.fetchall()

    print_table(rows, headers) 

def autors_livro(conn: pyodbc.Connection, table: str, schema: str = "dbo", livro: str = "", top: int = 100):
    # validação simples para evitar SQL injection em nomes
    import re
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", table) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", schema):
        raise ValueError("Invalid schema/table name")

    if livro:
        livro = f"%{livro}%" 
    else:
        livro = "%"

    sql = f"SELECT ISBN, titulo FROM [{schema}].livro WHERE titulo LIKE ?;"
    cur = conn.cursor()
    cur.execute(sql, (livro,))

    headers = [c[0] for c in cur.description]
    rows = cur.fetchall()
    print("Autores para os livros:")
    for row in rows:
        print(f" - {row.ISBN}: {row.titulo}")

    sql = (f"SELECT TOP ({top}) a.id_pessoa, a.nome, a.contacto, e.livro "
            f"FROM [{schema}].autor a "
                f"JOIN [{schema}].escreve e ON a.id_pessoa = e.autor "
            f"WHERE e.livro IN (SELECT ISBN FROM [{schema}].livro WHERE titulo LIKE ?);")

    cur = conn.cursor()
    cur.execute(sql, (livro,))

    headers = [c[0] for c in cur.description]
    rows = cur.fetchall()

    print_table(rows, headers) 
 

if __name__ == "__main__":
#   Testes estáticos para validação de ligação à base de dados e funcionalidade básica da DAO de Livro. 
#   Estes testes não são exaustivos e servem apenas para validação inicial. Não dispensam testes unitários, mais completos e estruturados,
#   nem testes de integração - em formato BDD ou equivalente - que devem ser implementados posteriormente para garantir a robustez e fiabilidade da aplicação.

#    test_db_connection()

    myDao = database.DAO()
    conn = myDao.connect()

    if conn:
        list_table(conn, "livro", "dbo")

    livro = input("Enter livro para pesquisar autor(es), 'ENTER' para todos: ")
    if conn:
        autors_livro(conn, "autor", "dbo", livro)

    print("\n--- Testando DAO de Livro ---")
    print("\nLista original de livros:\n")
    livros = LivroDAO().listar()
    tools.print_list(
        livros, 
        columns=["ISBN", "Titulo", "Idioma", "Tipo", "Tema", "Data_Publicacao"], 
        headers=["ISBN", "Título", "Idioma", "Tipo", "Tema", "Ano Publicação"]
    )

    dao = LivroDAO()

    livro = Livro(
        ISBN="9781234567890",
        Titulo="Introdução ao Python",
        idioma="PT-PT",
        tipo=["Manual", "Programação"],
        tema=["Python", "Bases de Dados"],
        data_publicacao=2024,
        editora=None
    )

    print("\nCriando livro de teste (ISBN = '9781234567890')...\n ")

    if dao.obter_por_isbn("9781234567890") is None:
        dao.criar(livro)

    print("\nLista com adição de livro de teste ordenada por orden ascendente de titulo:\n")
    livros = dao.listar(order_by="titulo", direction="ascendente")
    tools.print_list(
        livros, 
        columns=["ISBN", "Titulo", "Idioma", "Tipo", "Tema", "Data_Publicacao"], 
        headers=["ISBN", "Título", "Idioma", "Tipo", "Tema", "Ano Publicação"]
    )

    print("\n A mesma lista mas orden descendente de titulo:\n")
    livros = dao.listar(order_by="titulo", direction="desc")
    tools.print_list(
        livros, 
        columns=["ISBN", "Titulo", "Idioma", "Tipo", "Tema", "Data_Publicacao"], 
        headers=["ISBN", "Título", "Idioma", "Tipo", "Tema", "Ano Publicação"]
    )

    print("\nLista filtrada  por titulo (Python) e ordenadapor orden ascendente de titulo:\n")
    livros = dao.listar(filtros={"titulo": "Python"}, order_by="titulo", direction="asc")
    tools.print_list(
        livros, 
        columns=["ISBN", "Titulo", "Idioma", "Tipo", "Tema", "Data_Publicacao"], 
        headers=["ISBN", "Título", "Idioma", "Tipo", "Tema", "Ano Publicação"]
    )

    print("\nAlterar nome ao livro inserido (ISBN = '9781234567890')...\n ")  
    livro_existente = dao.obter_por_isbn("9781234567890")

    if livro_existente:
        livro_existente.Titulo = "Introdução ao Python - 2ª Edição"
        dao.atualizar(livro_existente)

    print("\nLista igual à última anterior mas com nome de livro alterado:\n")
    livros = dao.listar(filtros={"titulo": "Python"}, order_by="titulo", direction="asc")
    tools.print_list(
        livros, 
        columns=["ISBN", "Titulo", "Idioma", "Tipo", "Tema", "Data_Publicacao"], 
        headers=["ISBN", "Título", "Idioma", "Tipo", "Tema", "Ano Publicação"]
    )

    print("\nEliminar o livro inserido (ISBN = '9781234567890')...\n ")
    dao.apagar("9781234567890")   

    print("\nLista reposta ao original:\n")
    livros = LivroDAO().listar()
    tools.print_list(
        livros, 
        columns=["ISBN", "Titulo", "Idioma", "Tipo", "Tema", "Data_Publicacao"], 
        headers=["ISBN", "Título", "Idioma", "Tipo", "Tema", "Ano Publicação"]
    )    