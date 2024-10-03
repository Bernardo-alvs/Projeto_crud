import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = ' Bernardo' ,
    host = 'localhost' ,
    password = 'projeto123',
    db = 'projeto_crud'

)
if conn.is_connected():
    print('Conectado com sucesso!!!!')
else:
    print('Falha na conexão')
