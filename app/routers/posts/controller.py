from sqlalchemy.orm.session import Session

from app.sql_app import schemas
from app.sql_app.crud import post as post_crud


def get_posts(db: Session):
    db_data = post_crud.get_list(db)

    return schemas.Post(**db_data.__dict__)

def show_post(db: Session, id: int):
    db_data = post_crud.get(db, id)

    return schemas.Post(**db_data.__dict__)


def create_post(db: Session, data: schemas.PostCreate):
    db_data = post_crud.add(db, data)

    return schemas.Post(**db_data.__dict__)


def update_post(db: Session, data: schemas.PostUpdate):
    db_data = post_crud.update(db, data)

    return schemas.Post(**db_data.__dict__)


def delete_post(db: Session, id: int):
    db_data = post_crud.delete(db, id)

    return db_data