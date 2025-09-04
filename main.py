from fastapi import FastAPI

from apps import include_router
from database import run_migrations

app = FastAPI(title="Project Demo", version="1.0.0")

# Base.metadata.create_all(bind=engine)

run_migrations()

include_router(app)

@app.get("/")
def root():
  return {"Hello World"}
