from app.db.base import Base
from sqlalchemy import UUID, String, ARRAY, Integer
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(70), nullable=False)

# check name column type_device
