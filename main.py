from fastapi import FastAPI
from database import Base, engine, run_migrations
from apps import include_router

app = FastAPI(title="Project Demo", version="1.0.0")

# Base.metadata.create_all(bind=engine)

run_migrations()

include_router(app)

@app.get("/")
def root():
  return {"Hello World"}