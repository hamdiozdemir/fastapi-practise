from fastapi import FastAPI, status, Response
from routers import blog, blog_post, param, user, article
from typing import Optional
from db import models
from db.database import engine


app = FastAPI()
app.include_router(blog.router)
app.include_router(blog_post.router)
app.include_router(param.router)
app.include_router(user.router)
app.include_router(article.router)



@app.get('/')
def index():
    return {"Hello": "World"}



models.Base.metadata.create_all(engine)
