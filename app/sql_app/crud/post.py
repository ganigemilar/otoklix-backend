from sqlalchemy.orm.session import Session

from app.sql_app import models, schemas


def add(db: Session, data: schemas.PostCreate):
    db_data = models.Post(**data.dict())

    db.add(db_data)
    db.commit()
    db.refresh(db_data)

    return db_data


def get(db: Session, id: int):
    q = db.\
        query(models.Post).\
        filter(models.Post.id == id)

    return q.first()


def update(db: Session, data: schemas.PostUpdate):
    db_data = get(db, data.id)

    if not db_data:
        raise Exception("no data found!")

    data_updates = data.dict(exclude_unset=True)
    for key, value in data_updates.items():
        setattr(db_data, key, value)
    db.commit()
    db.refresh(db_data)

    return db_data


def delete(db: Session, id: int):
    db_data = get(db, id)

    if not db_data:
        raise Exception("no data found!")

    db.delete(db_data)
    db.commit()

    return True


def get_list(db: Session):
    q = db.\
        query(models.Post)

    return q.all()