from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

state = {
    "post_id": None
}

post_dummy = {
    "title": "Hello cui",
    "content": "Hello world dang dang"
}

post_update_dummy = {
    "title": "coba ya",
    "content": "coba aja say"
}


def test_get_posts():
    response = client.get("/posts")

    assert response.status_code == 200


def test_create_post():
    response = client.post("/posts", json=post_dummy)

    assert response.status_code == 201
    assert response.json()["title"] == post_dummy["title"]
    assert response.json()["content"] == post_dummy["content"]
    
    if response.content:
        json = response.json()
        state["post_id"] = json["id"]


def test_show_post():
    response = client.get("/posts/{}".format(state["post_id"]))

    assert response.status_code == 200
    assert response.json()["id"] == state["post_id"]
    assert response.json()["title"] == post_dummy["title"]
    assert response.json()["content"] == post_dummy["content"]


def test_update_post():
    response = client.put("/posts/{}".format(state["post_id"]), json=post_update_dummy)

    assert response.status_code == 200
    assert response.json()["id"] == state["post_id"]
    assert response.json()["title"] == post_update_dummy["title"]
    assert response.json()["content"] == post_update_dummy["content"]


def test_delete_post():
    response = client.delete("/posts/{}".format(state["post_id"]))

    assert response.status_code == 200
