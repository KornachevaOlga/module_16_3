



from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


# @app.post("/user/{username}/{age}")
# async def create_user(username: str, age: int):
#     user_id = str(int(max(users, key=int)) + 1)
#     users[user_id] = f"Имя: {username}, возраст: {age}"
#     return f"User {user_id} is registered"

@app.post('/user/{username}/{age}')
async def post_user(
    username: Annotated[str, Path(min_length=5, max_length=20,
                                  description='Enter username', example='UrbanUser')],
    age: Annotated[int, Path(le=120, ge=18, description='Enter age', example='24')]
):
    user_id = str(int(max(users, key=int)) + 1)
    users.update({user_id: f'Имя: {username}, возраст: {age}'})
    return f'User {user_id} is registered'



@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    del users[user_id]
    return f"User {user_id} has been deleted"

# from typing import Annotated
# from fastapi import FastAPI, Path
#
# app = FastAPI()
#
# users = {'1': 'Имя: Example, возраст: 18'}
#
#
# @app.get("/users")
# async def get_users() -> dict:
#     return users
#
#
# @app.post("/user/{username}/{age}")
# async def create_user(username: Annotated[str, Path(min_length=5,
#                                                     max_length=30,
#                                                     description="Enter username",
#                                                     example="UrbanUser")],
#                       age: Annotated[int, Path(ge=18,
#                                                le=120,
#                                                description="Enter age",
#                                                example="24")]) -> str:
#     current_id = str(int(max(users, key=int)) + 1)
#     users[current_id] = f"Имя: {username}, возраст: {age}"
#     return f"The user {current_id} is registered"
#
#
# @app.put("/user/{user_id}/{username}/{age}")
# async def update_user(user_id: Annotated[int, Path(ge=0,
#                                                    le=1000000,
#                                                    description="Enter user_id",
#                                                    example="24")],
#                       username: Annotated[str, Path(min_length=5,
#                                                     max_length=30,
#                                                     description="Enter username",
#                                                     example="UrbanUser")],
#                       age: Annotated[int, Path(ge=18,
#                                                le=120,
#                                                description="Enter age",
#                                                example="24")]) -> str:
#     users[str(user_id)] = f"Имя: {username}, возраст: {age}"
#     return f"The user {user_id} has been updated"
#
#
# @app.delete("/user/{user_id}")
# async def delete_user(user_id: Annotated[int, Path(ge=0,
#                                                    le=1000000,
#                                                    description="Enter user_id",
#                                                    example="24")]) -> str:
#     users.pop(str(user_id))
#     return f"The user {user_id} has been deleted"