from app.api.schemas.device import PostDeviceRequest
from app.db.models.device import Device
from app.db.repository.device import DeviceRepository
from sqlalchemy.orm import Session

from typing import Type
import uuid


def get_device_by_name(device_id: uuid.UUID, session: Session) -> Type[Device] | None:
    device_repo = DeviceRepository(session)

    device = device_repo.get_device(device_id=device_id)

    if device:
        return device


def post_device_(data: PostDeviceRequest, session: Session) -> Device | None:
    device_repo = DeviceRepository(session)

    device = device_repo.post_device(
        name=data.name,
        type_device=data.type_device,
        type_value=data.type_value,
        range_value=data.range_value,
        current_value=data.current_value,
    )

    if device:
        return device


def delete_device_by_name(
    device_id: uuid.UUID, session: Session
) -> Type[Device] | None:
    device_repo = DeviceRepository(session)

    device = device_repo.delete_device(device_id=device_id)

    if device:
        return device
