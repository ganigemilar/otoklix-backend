from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from . import controller
from app.sql_app.database import get_db
from app.sql_app import schemas


router = APIRouter()

@router.get("", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    result = controller.get_posts(db)

    return result


@router.get("/{id}", response_model=schemas.Post)
def show_post(id: int, db: Session = Depends(get_db)):
    result = controller.show_post(db, id)

    return result


@router.post("", response_model=schemas.Post)
def create_post(data: schemas.PostCreate, db: Session = Depends(get_db)):
    result = controller.create_post(db, data)

    return result


@router.put("/{id}")
def update_post(id: int, data: schemas.PostUpdate, db: Session = Depends(get_db)):
    data.id = id
    
    result = controller.update_post(db, data)

    return result


@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    result = controller.delete_post(db, id)

    return result