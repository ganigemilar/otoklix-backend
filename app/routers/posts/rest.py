from fastapi import APIRouter


router = APIRouter()

@router.get("/posts")
def get_posts():
    pass


@router.get("/posts/{id}")
def show_post():
    pass


@router.post("/posts")
def create_post():
    pass


@router.put("/posts/{id}")
def update_post():
    pass


@router.delete("/posts/{id}")
def delete_post():
    pass