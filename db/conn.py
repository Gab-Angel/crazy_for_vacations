import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

load_dotenv()

def connection():
    try:
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            password=os.getenv("DB_PASSWORD"),
            cursor_factory=psycopg2.extras.RealDictCursor
        )
    except:
        print("Erro ao se conectar ao BD")

if __name__ == "__main__":
    connection()