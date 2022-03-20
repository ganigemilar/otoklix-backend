from fastapi import FastAPI

from app.sql_app.database import engine
from app.sql_app import models
from app.routers.posts import rest as posts_rest


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    router=posts_rest.router,
    prefix="/posts",
    tags=["Post API"]
)