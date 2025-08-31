from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import time
import os

load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

for i in range(10):
  try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    connection.close()
    break
  except exc.OperationalError:
    print("⏳ Banco ainda não está pronto, tentando novamente...")
    time.sleep(3)
else:
    raise Exception("❌ Não foi possível conectar ao banco de dados.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()