from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.schemas.device import (
    GetDeviceResponse,
    PostDeviceRequest,
    PostDeviceResponse,
    DeleteDeviceResponse,
)
from app.api.core.device import (
    delete_device_by_name,
    get_device_by_name,
    post_device_,
)

import uuid


device_router = APIRouter()


@device_router.get("/{device_id}")
def get_device(
    device_id: uuid.UUID, db: Session = Depends(get_db)
) -> GetDeviceResponse:
    device = get_device_by_name(device_id, session=db)

    if not device:
        raise HTTPException(
            status_code=404, detail=f"Device by name {device_id} not found"
        )

    return GetDeviceResponse(
        device_id=device.device_id,
        name=device.name,
        type_device=device.type_device,
        type_value=device.type_value,
        range_value=device.range_value,
        current_value=device.current_value,
    )


@device_router.post("/")
def post_device(
    body: PostDeviceRequest, db: Session = Depends(get_db)
) -> PostDeviceResponse:
    device = post_device_(body, session=db)

    if not device:
        raise HTTPException(status_code=400, detail="Unknown error")

    return PostDeviceResponse(
        device_id=device.device_id,
        name=device.name,
    )


@device_router.delete("/{device_id}")
def delete_device(
    device_id: uuid.UUID, db: Session = Depends(get_db)
) -> DeleteDeviceResponse:
    device = delete_device_by_name(device_id, session=db)

    if not device:
        raise HTTPException(
            status_code=404, detail=f"Device with ID {device_id} not found"
        )

    return DeleteDeviceResponse(
        device_id=device.device_id,
        name=device.name,
    )
