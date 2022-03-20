from sqlalchemy.orm.session import Session

from app.sql_app import schemas
from app.sql_app.crud import post as post_crud


def get_posts(db: Session):
    db_data = post_crud.get_list(db)

    if not db_data:
        return []

    result = [schemas.Post(**v.__dict__) for v in db_data]

    return result

def show_post(db: Session, id: int):
    db_data = post_crud.get(db, id)

    if not db_data:
        return None

    result = schemas.Post(**db_data.__dict__)

    return result


def create_post(db: Session, data: schemas.PostCreate):
    db_data = post_crud.add(db, data)

    result = schemas.Post(**db_data.__dict__)

    return result


def update_post(db: Session, data: schemas.PostUpdate):
    db_data = post_crud.update(db, data)

    result = schemas.Post(**db_data.__dict__)

    return result


def delete_post(db: Session, id: int):
    db_post = post_crud.get(db, id)

    if not db_post:
        raise Exception("data not found!")

    post_crud.delete(db, id)

    result = schemas.Post(**db_post.__dict__)
    
    return result