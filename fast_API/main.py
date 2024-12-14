from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from fast_API.schemas import Message, UserSchemas, UserPublic, UserDB, UserList

app = FastAPI()

database = []

@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message":"Olá Mundo"}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_users(user: UserSchemas):
    
    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump()
    )

    database.append(user_with_id)

    return user_with_id

@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}

@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchemas):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User Not found"
        )

    user_with_id = UserDB( **user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User Not found"
        )
    
    user_with_id = database[user_id - 1]
    del database[user_id - 1]

    return {"message": 'User Deleted'}
