import os
from dotenv import load_dotenv
import mysql.connector

# Carrega variáveis do .env
load_dotenv()

config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': int(os.getenv("DB_PORT", 21455)),  # porta padrão se não estiver no .env
    'database': os.getenv("DB_NAME"),
    'ssl_ca': os.getenv("DB_SSL_CA")
}

# Função para criar conexão
def get_connection():
    return mysql.connector.connect(**config)

# Função para criar a tabela se não existir
def criar_tabela():
    con = get_connection()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS historico (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario VARCHAR(255),
        mensagem TEXT,
        tipo VARCHAR(20),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    con.commit()
    cur.close()
    con.close()

# Função para salvar mensagem no histórico
def salvar_historico(usuario, mensagem, tipo):
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO historico (usuario, mensagem, tipo) VALUES (%s, %s, %s)",
        (usuario, mensagem, tipo)
    )
    con.commit()
    cur.close()
    con.close()

# Função para buscar todas as mensagens
def buscar_historico():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT id, usuario, mensagem, tipo, timestamp FROM historico ORDER BY timestamp DESC")
    dados = cur.fetchall()
    cur.close()
    con.close()
    return dados
