import datetime 
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from db.models import DbPost
from route.schemas import PostBase, PostDisplay


def create_post(db : Session, request: PostBase):
    new_post = DbPost(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_post(db : Session, id : int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    return post

def get_all_post(db: Session):
    all_post = db.query(DbPost).all()
    return all_post


def update_post(db: Session, id : int, request: PostDisplay):
    post = db.query(DbPost).filter(DbPost.id == id)
    post.update({
        DbPost.image_url : request.image_url,
        DbPost.title : request.title,
        DbPost.content : request.content,
        DbPost.creator : request.creator
    })
    db.commit()
    return "update completed"


def delete_post(db: Session, id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    db.delete(post)
    db.commit()
    return "deleted"