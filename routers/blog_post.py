from typing import Optional, List, Dict
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


# Custom model
class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    is_published: Optional[bool]
    nb_comments: int
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': "val1"}
    # List
    # Set
    # Dict
    # Tuple
    image: Optional[Image] = None





@router.post('/new')
def create_blog(blog: BlogModel):
    return blog


@router.post('/new/{id}')
def create_blog_with_params(blog: BlogModel, id: int, version: int = 1):
    return {
        'data': blog,
        'id': id,
        'version': version
    }


@router.post('/new/{id}/comment')
def create_comment_for_blog(blog: BlogModel,
                            id: int,
                            comment_id: int = Query(None,
                                                    title='Custom ID of comment',
                                                    description='Some description',
                                                    alias='commentId'
                                                    )):
    return {
        'data': blog,
        'id': id,
        'comment_id': comment_id
    }


# a default value for body
@router.post('/body/{id}')
def create_body_param(blog: BlogModel,
                      id: int,
                      content: str = Body('Hi this is Body')):
    return {
        'data': blog,
        'id': id,
        'content': content
    }


# non default value with ...
@router.post('/body-required')
def create_body_with_required(blog: BlogModel,
                              id: int,
                              content: str = Body(...)):
    return {
        'data': blog,
        'id': id,
        'content': content
    }


# min_len validator for body or others
@router.post('/body-required-validator')
def create_body_with_required(blog: BlogModel,
                              id: int,
                              content: str = Body(...,
                                                  min_length=10)): # max_length de olur
    return {
        'data': blog,
        'id': id,
        'content': content
    }


# multiple query params
@router.post("/query-list")
def query_by_list(blog: BlogModel,
                  v: List[str] = Query(None)):
    print(v)
    return {
        'data': blog,
        'version': v
    }


# number validator -> comment_id : int = Path(None, gt=5)  -ge=5, -lt=5, -le=5


@router.post("/path_number_validator/{id}/comment/{comment_id}")
def path_number_validator(blog: BlogModel, id: int,
                          comment_id : int = Path(gt=5, le=10)):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id
    }


# DEPENDENCIES
# used in param.py
def required_functionalities():
    print("Required Functionalities worked.")
    return {'message': 'Learning FastAPI'}