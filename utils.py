import cx_Oracle
import json

def conecta_banco(user,senha,dsn):
    try:
        conn = cx_Oracle.connect(user=user, password=senha, dsn=dsn)
        print("Conectado na primeira tentativa")

    except Exception as ex:
        print(f"Erro da ({ex}) primeira tentativa .. tentando segunda forma")
        cx_Oracle.init_oracle_client(lib_dir=r"P:\instantclient-basic-windows.x64-21.11.0.0.0dbru\instantclient_21_11")
        conn = cx_Oracle.connect(user=user, password=senha, dsn=dsn)
    finally:
        print("Conectado!")

    return conn

def cria_dsn(host,port,sid):
    dsn = cx_Oracle.makedsn(host = host, port=port, sid=sid)

    return dsn

def carrega_credenciais(path ="credenciais.json"):
    with open(path, "r") as arquivo:
        dados = json.load(arquivo)
    user = dados["user"]
    senha = dados["senha"]

    return user,senha

#função para limpar todos os dados da tabela
def limpa_tabela_toda(cursor, conn, tabela = "TB_USUARIO"):
    cursor.execute(f"DELETE FROM {tabela}")
    conn.commit()

#função para Criar alterar e deletar informações da tabela
def cud(cursor, conn, query, valores): 
    cursor.execute(query,valores)
    conn.commit()

#função para inserir informações na tabela
def create(cursor, conn,id,nome):
    #Estrutura de repetição para a pessoa alterar o id caso ele já exista
    while True:
        try:
            valores = (id, nome)
            query = "INSERT INTO TB_USUARIO (ID, NOME) VALUES (:valor1,:valor2)"
            cursor.execute(query,valores)
            conn.commit()
            break
        except cx_Oracle.IntegrityError as ex:
            print("XXXX - Não foi possivel inserir este ID, ID já existente na tabela!")
            print(ex)
            id = int(input("Escolha um novo valor para ID"))

#função para alterar informações na tabela
def update(cursor, conn,id,nome):
    valores = (nome, id)
    query = "UPDATE TB_USUARIO SET NOME=:valor1 WHERE ID=:valor2"
    cursor.execute(query,valores)
    conn.commit()

#função para deletar informações na tabela
def delete(cursor, conn,id):
    valor = (id,)#tupla de tamanho 1 (OBRIGATÓRIAMENTE TEM QUE SER UMA TUPLA)
    query = "DELETE FROM TB_USUARIO WHERE ID=:valor1"
    cursor.execute(query,valor)
    conn.commit()

#função para ler as linhas da tabela
def ler_Tabela_toda(cursor):
    query = "SELECT * FROM TB_USUARIO"
    cursor.execute(query)
    linhas = cursor.fetchall()
    return linhas