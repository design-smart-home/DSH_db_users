from pydantic import BaseModel
from typing import List
import uuid


# class GetDeviceRequest(BaseModel):
#     device_id: uuid.UUID
#     name: str
#     type_device: str
#     range_value: List[int]
#     current_value: int


class GetDeviceResponse(BaseModel):
    device_id: uuid.UUID
    name: str
    type_device: str
    type_value: str
    range_value: List[int]
    current_value: int


class PostDeviceRequest(BaseModel):
    name: str
    type_device: str
    type_value: str
    range_value: List[int]
    current_value: int


class PostDeviceResponse(BaseModel):
    device_id: uuid.UUID
    name: str


class DeleteDeviceRequest(BaseModel):
    device_id: uuid.UUID


class DeleteDeviceResponse(BaseModel):
    device_id: uuid.UUID
    name: str
