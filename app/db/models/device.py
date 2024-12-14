from app.db.base import Base
from sqlalchemy import UUID, String, ARRAY, Integer
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Device(Base):
    __tablename__ = "devices"

    device_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    type_device: Mapped[str] = mapped_column(String(6), nullable=False)
    type_value: Mapped[str] = mapped_column(String(10), nullable=False)
    range_value: Mapped[list[int]] = mapped_column(ARRAY(Integer), nullable=False)
    current_value: Mapped[int] = mapped_column(Integer(), nullable=False)


# check name column type_device
