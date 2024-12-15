from app.api.schemas.user import PostUserRequest
from app.db.models.user import User
from app.db.repository.user import UserRepository
from sqlalchemy.orm import Session

from typing import Type
import uuid


def get_user_by_id(user_id: uuid.UUID, session: Session) -> Type[User] | None:
    user_repo = UserRepository(session)

    user = user_repo.get_user(user_id=user_id)

    if user:
        return user


def post_user_(data: PostUserRequest, session: Session) -> User | None:
    device_repo = UserRepository(session)

    user = device_repo.post_user(
        username=data.username,
        email=data.email,
        hashed_password=data.hashed_password,
    )

    if user:
        return user


def delete_user_by_id(
    user_id: uuid.UUID, session: Session
) -> Type[User] | None:
    user_repo = UserRepository(session)

    user = user_repo.delete_user(user_id=user_id)

    if user:
        return user
