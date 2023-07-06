from fastapi import FastAPI

from user.models import User
from poll.models import Poll

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "ok"}


@app.get("/polls")
async def root():
    return {"polls": "ok"}


@app.get("/users")
async def root():
    return {"users": "ok"}


@app.post("/users/")
async def create_user(user: User):
    return user


@app.post("/polls/")
async def create_poll(poll: Poll):
    return poll