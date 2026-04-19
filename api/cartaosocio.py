import sqlite3
import random
from datetime import datetime

def criar_socio_automatico(dados):
    numero_gerado = f"{random.randint(1000, 9999)}-2026"
    ano_atual = datetime.now().year
    db_connection = sqlite3.connect("benfica.db")
    cursor = db_connection.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO socios (
                nome_completo, email, telemovel, morada, 
                localidade, codigo_postal, numero_socio, desde, pontos
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 500)
        """, (
            dados['nome'], 
            dados['email'], 
            dados['telemovel'], 
            dados['morada'], 
            dados['localidade'], 
            dados['cp'],
            numero_gerado,
            ano_atual
        ))
        
        db_connection.commit()
        db_connection.close()

        return {
            "numero_socio": numero_gerado,
            "desde": ano_atual,
            "pontos": 500,
            "status": "sucesso"
        }
    except:
        return {"status": "erro"}

def consultar_socio_pelo_numero(numero_socio):
    db_connection = sqlite3.connect("benfica.db")
    db_connection.row_factory = sqlite3.Row
    cursor = db_connection.cursor()
    
    try:
        cursor.execute("SELECT * FROM socios WHERE numero_socio = ?", (numero_socio,))
        socio = cursor.fetchone()
        db_connection.close()
        
        if socio:
            return {
                "status": "sucesso",
                "dados_cartao": {
                    "nome": socio['nome_completo'],
                    "numero_socio": socio['numero_socio'],
                    "desde": socio['desde'],
                    "pontos": socio['pontos'],
                    "tipo": "SÓCIO RED"
                }
            }
        else:
            return {
                "status": "erro", 
                "mensagem": "Número de sócio não encontrado."
            }
            
    except Exception as e:
        return {
            "status": "erro", 
            "mensagem": f"Erro na consulta: {str(e)}"
        }