import psycopg

conn = psycopg.connect("dbname='IFit' user='postgres' host='localhost' password='123'")
cur = conn.cursor()

def conectar():
    global conn, cur
    try:
        conn = psycopg.connect("dbname='IFit' user='postgres' host='localhost' password='123'")
        cur = conn.cursor()
    except psycopg.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        exit(1)

def verificar_conexao():
    global conn, cur
    try:
        cur.execute("SELECT 1")
    except psycopg.Error:
        print("Conexão perdida. Reconectando...")
        conectar()