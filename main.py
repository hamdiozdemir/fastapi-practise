from fastapi import FastAPI, Request, HTTPException
from routers import blog, blog_post, param, user, article, product, file
from auth import authentication
from typing import Optional
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(blog.router)
app.include_router(blog_post.router)
app.include_router(param.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


# CORS Middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = ['http://localhost:3000'],
#     allow_credentials = True,
#     allow_methods = ['*']
#     allow_headers = ['*']
# )


@app.get('/')
def index():
    return {"Hello": "World"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )


# This overrides all the exceptions bcoz --> HTTPExceptions
# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)

app.mount('/files', StaticFiles(directory='files'), name='files')
