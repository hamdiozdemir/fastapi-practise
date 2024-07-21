from typing import List
from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)


# list users
@router.get('/', response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
        # Handle exceptions
    return db_user.get_all_users(db)


# retrieve user
@router.get('/{id}', response_model=UserDisplay)
def retrieve_user(id: int, db: Session = Depends(get_db)):
        # Handle exceptions
    return db_user.retrieve_user(db, id)

# update user
@router.post('/{id}/update', response_model=UserDisplay)
def update_user(id:int, request: UserBase, db: Session = Depends(get_db)):
        # Handle exceptions
    return db_user.update_user(db, id, request)

# delete user
@router.get('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
        # Handle exceptions
    return db_user.delete_user(db, id)
