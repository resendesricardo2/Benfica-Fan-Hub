import sqlite3

db_connection = sqlite3.connect("benfica.db")
cursor = db_connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS socios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_completo TEXT NOT NULL, email TEXT UNIQUE NOT NULL, telemovel TEXT, morada TEXT, localidade TEXT, codigo_postal TEXT, numero_socio TEXT, desde INTEGER, pontos INTEGER DEFAULT 500)")
db_connection.commit()
db_connection.close()
print("Base de dados do Benfica criada com sucesso!")