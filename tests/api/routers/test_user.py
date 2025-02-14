import uuid

import pytest

from app.db.models.user import User


@pytest.fixture
def params():
    return {
        "user_id": str(uuid.uuid4()),
        "username": "test_user",
        "email": "test@email.ru",
        "hashed_password": "test_password",
    }


def test_create_user_in_db(db, create_user_in_db, params):
    create_user_in_db(
        user_id=params["user_id"],
        username=params["username"],
        email=params["email"],
        hashed_password=params["hashed_password"],
        session=db,
    )

    user = db.query(User).filter(User.user_id == params["user_id"]).first()

    assert user is not None


def test_post_user(db, client, params):
    response = client.post(f"users/", json=params)

    assert response.status_code == 200
    assert response.json()["username"] == params["username"]

    user = db.query(User).filter(User.user_id == response.json()["user_id"]).first()

    assert user is not None


def test_get_user(db, client, create_user_in_db, params):
    create_user_in_db(**params, session=db)

    response = client.get(f"users/{params['user_id']}")

    assert response.status_code == 200
    assert response.json() == {
        "user_id": params["user_id"],
        "username": params["username"],
        "email": params["email"],
        "hashed_password": params["hashed_password"],
    }


def test_delete_user(db, client, create_user_in_db, params):
    create_user_in_db(**params, session=db)

    response = client.delete(f"users/{params['user_id']}")

    assert response.status_code == 200

    user = db.query(User).filter(User.user_id == params["user_id"]).first()

    assert user is None
