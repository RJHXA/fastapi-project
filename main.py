from fastapi import FastAPI
from database import Base, engine

app = FastAPI(title="Project Demo", version="1.0.0")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
  return {"message": "Welcome to FastAPI Demo"}