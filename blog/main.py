from fastapi import FastAPI

from model import Blog

app = FastAPI()


@app.post("/blog")
def create(request: Blog):
    return request
