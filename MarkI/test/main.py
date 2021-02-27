from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Cria aplicação
app = FastAPI()

# Rota raiz
@app.get("/")
def raiz():
  return {"Hello": "World"}

# Model
class User(BaseModel):
  id: int
  mail: str
  password: str

# Base de dados

bd = [
  User(id=1, mail='yurilima95@gmail.com', password='idk'),
  User(id=2, mail='yuri@snackin.co', password='idk2')
]

# Rota Get All
@app.get("/User")
def get_all_user():
  return bd

# Rota Get Id
@app.get("/User/{user_id}")
def get_user_by_id(user_id: int):
  for user in bd:
    if(user.id == user_id):
      return user
  return {"Status": 404, "Message": "User not found"}

# Rota de inserir
@app.post("/User")
def post_user(user: User):
  bd.append(user)
  return user
