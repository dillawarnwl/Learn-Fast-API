from os import terminal_size
from fastapi import FastAPI
from pydantic_core import Url

app = FastAPI()
@app.get("/home")
def home():
    return {"message":"Alhumdulilah! I have created my first API"}

posts = {
    'title':"Ehsas",
    'description':"Ehsas Lab for Like minded people."}
@app.get("/posts")
def get_posts():
    return posts
