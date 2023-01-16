import shutil
from typing import List
from route.schemas import PostBase, PostDisplay
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_post
import string
import random

router = APIRouter(
    prefix='/post',
    tags=['post']
)

@router.get('/all')
def get_all_post(db: Session = Depends(get_db)):
    return db_post.get_all_post(db)

@router.post('/')
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create_post(db, request)

@router.get('/{id}')
def get_post(id : int, db: Session = Depends(get_db)):
    return {
        'data' : db_post.get_post(db, id)
    }

@router.put('/update/{id}')
def update_post(id: int, request: PostBase, db: Session = Depends(get_db)):
    return db_post.update_post(db, id, request)


@router.delete('/delete')
def delete_post(id : int, db: Session = Depends(get_db)):
    return db_post.delete_post(db, id)

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}'

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {'filename' : path}