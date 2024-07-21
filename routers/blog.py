from typing import Optional

from fastapi import APIRouter, status, Response

from enums import BlogType

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get('/all',
            summary='Retrieve all blogs',
            description='This API calls all the blog objects.',
            response_description='Returns all the blogs in response.'
            )
def blog_list():
    return {"blogs": [
        {"id": 1, "title": "Blog 1"},
        {"id": 2, "title": "Blog 2"},
    ]}


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type is {type}'}


@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Get comments from specific blog ID

    - ***id***: required id of blog
    - ***comment_id:*** required id of comment
    - ***valid:*** optional bool
    - ***username:*** optional string username
    """
    return {
        'message': f'blog_id: {id}, comment_id: {comment_id}, valid: {valid}, username: {username}'
    }


@router.get('/{id}', status_code=status.HTTP_200_OK)
def blog_detail(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Blog {id} not found'}
    return {"ID": f"Your id is {id}"}

