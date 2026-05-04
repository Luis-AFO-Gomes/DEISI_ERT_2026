import dao
import pyodbc

def test_db_connection():
    """
    Tests the database connection by attempting to connect and printing the result.
    """
    myDao = dao.DAO()
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
#    test_db_connection()

    myDao = dao.DAO()
    conn = myDao.connect()

    if conn:
        list_table(conn, "livro", "dbo")

    livro = input("Enter livro para pesquisar autor(es), 'ENTER' para todos: ")
    if conn:
        autors_livro(conn, "autor", "dbo", livro)