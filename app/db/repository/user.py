from sqlalchemy.orm import Session

from app.db.models.user import User
from typing import Type, List
import uuid


class UserRepository:
    def __init__(self, db: Session):
        self._db = db

    def get_user(self, user_id: uuid.UUID) -> Type[User] | None:
        user = self._db.query(User).filter(User.user_id == user_id).first()

        if user:
            return user

    def post_user(
        self,
        username: str,
        email: str,
        hashed_password: str,
    ) -> User:
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
        )

        self._db.add(user)
        self._db.commit()
        self._db.flush()

        return user

    def delete_user(self, user_id: uuid.UUID) -> Type[User] | None:
        user = self._db.query(User).filter(User.user_id == user_id).first()

        if user:
            self._db.delete(user)
            self._db.commit()
            self._db.flush()

            return user
