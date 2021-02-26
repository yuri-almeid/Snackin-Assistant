from fastapi import FastAPI
from pydantic import BaseModel

# Cria aplicação
app = FastAPI()

# Rota raiz
@app.get("/")
def raiz():
  return {"Hello": "World"}