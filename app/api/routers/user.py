from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.schemas.user import (
    GetUserResponse,
    PostUserRequest,
    PostUserResponse,
    DeleteUserResponse,
)
from app.api.core.user import (
    delete_user_by_id,
    get_user_by_id,
    post_user_,
)

import uuid


user_router = APIRouter()


@user_router.get("/{user_id}")
def get_user(
    user_id: uuid.UUID, db: Session = Depends(get_db)
) -> GetUserResponse:
    user = get_user_by_id(user_id, session=db)

    if not user:
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
        )

    return GetUserResponse(
        user_id=user.user_id,
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password,
    )


@user_router.post("/")
def post_user(
    body: PostUserRequest, db: Session = Depends(get_db)
) -> PostUserResponse:
    user = post_user_(body, session=db)

    if not user:
        raise HTTPException(status_code=400, detail="Unknown error")

    return PostUserResponse(
        user_id=user.user_id,
        username=user.username,
    )


@user_router.delete("/{user_id}")
def delete_user(
    user_id: uuid.UUID, db: Session = Depends(get_db)
) -> DeleteUserResponse:
    user = delete_user_by_id(user_id, session=db)

    if not user:
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
        )

    return DeleteUserResponse(
        user_id=user.user_id,
        username=user.username,
    )
