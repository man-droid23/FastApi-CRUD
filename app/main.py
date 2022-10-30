from fastapi import FastAPI, status, HTTPException, Response, Depends
from . import models, schemas, utils
from .database import engine, get_db
from . routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "hello world"}

