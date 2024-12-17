from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Инициализация FastAPI
app = FastAPI()

# Список пользователей
users = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# GET запрос - возвращает список всех пользователей
@app.get("/users")
def get_users():
    return users

# POST запрос - добавляет нового пользователя
@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    new_id = users[-1].id + 1 if users else 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user

# PUT запрос - обновляет существующего пользователя по его id
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос - удаляет пользователя по его id
@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail="User was not found")
