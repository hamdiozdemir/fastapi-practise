from typing import Optional, Dict
from routers.blog_post import required_functionalities
from fastapi import APIRouter, status, Response, Depends


router = APIRouter(
    prefix='/params',
    tags=['params']
)


@router.get('/params')
def get_params(page = 1, page_size = 10):
    return {'message': f'Page Size: {page_size}, on page: {page}'}


@router.get('/optional')
def get_optional_params(page: Optional[int] = None, page_size=5,
                        req_parameter: dict = Depends(required_functionalities)):
    return {'message': f'Page is {page} and page size is: {page_size}',
            'req': req_parameter}
