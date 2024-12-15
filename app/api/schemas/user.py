from pydantic import BaseModel
from typing import List
import uuid


# class GetUserRequest(BaseModel):
#     device_id: uuid.UUID
#     name: str
#     type_device: str
#     range_value: List[int]
#     current_value: int


class GetUserResponse(BaseModel):
    user_id: uuid.UUID
    username: str
    email: str
    hashed_password: str


class PostUserRequest(BaseModel):
    username: str
    email: str
    hashed_password: str


class PostUserResponse(BaseModel):
    user_id: uuid.UUID
    username: str


class DeleteUserRequest(BaseModel):
    user_id: uuid.UUID


class DeleteUserResponse(BaseModel):
    user_id: uuid.UUID
    username: str
