from utils import *
import requests

dsn = cria_dsn(host ='oracle.fiap.com.br', port=1521, sid='ORCL')

user, senha = carrega_credenciais()
conn = conecta_banco(user,senha,dsn)


#Criando o cursor (instancia para carregar as ações)
cursor = conn.cursor()

#INSERINDO VALORES NA TABELA
# cursor.execute("INSERT INTO TB_USUARIO (ID,NOME) VALUES (:valor1,:valor2)", valor1=1, valor2="Junior")
conn.commit()

#Eu posso entregar os valores para o cursor na forma de tupla:
#o python vai utilizar os valores na mesma ordem que foram escritos
# valores = (3,"Carlos")
# query = "INSERT INTO TB_USUARIO (ID, NOME) VALUES (:valor1,:valor2)"
# cursor.execute(query,valores)
# conn.commit()



#limpar a tabela (CUIDADO, ISTO SEMPRE LIMPA TODA A TABELA!)
#limpa_tabela_toda(cursor,conn) #O IDEAL É USAR O WHERE E PASSAR VALORES

#testando as funções
# create(cursor, conn, 5,"Miguel")
# update(cursor, conn, 4,"Julio")
# delete(cursor, conn, 6)

#CONSULTANDO A QUANTIDADE DE LINHAS DA TABELA
linhas_da_tabela = ler_Tabela_toda(cursor)
print(f"Esta tabela tem {len(linhas_da_tabela)} linhas!")
for linha in linhas_da_tabela:
    print(linha)

# cursor.close()


##Exercicio:
#pensar na estrutura da tabela que vamos criar
#pensar em pseudo-código/fluxograma os passos necessários para fazer o que estamos propondo
#(pegar a informação da API, pegar a informação da tabela, processar os dados e escrever na tabela)
#link api (https://home.openweathermap.org/users/sign_up)

#RECEBENDO DADOS

key = '2445e34b0549d9e82137ece6efae1ed7'
lat = -23.563886 
lon = -46.6529712
units = "metric"
endpoint=(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={key}")

resposta = requests.request("GET",endpoint)
print(resposta)
resposta_json = resposta.json()

#pegando os dados da chave "main"
main = resposta_json["main"]
temp = main["temp"]
temp_min = main["temp_min"]
temp_max = main["temp_max"]
print(temp)
print(temp_min)
print(temp_max)

#pegando os dados da chave "weather"
#lembrando que, pela documentação, vimos que é uma lista

weather = resposta_json["weather"][0]
clima = weather["main"]
print(clima)