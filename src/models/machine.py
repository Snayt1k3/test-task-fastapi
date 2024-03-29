import random
import string

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, orm
from src.db.db import Base
from src.dto.machine import MachineSchema


class Machine(Base):
    __tablename__ = "machines"

    id: Mapped[int] = mapped_column(primary_key=True)
    """Идентификатор в бд"""
    identifier: Mapped[str] = mapped_column(
        String(5),
        default=lambda: str(random.randint(1000, 9999))
        + random.choice(string.ascii_uppercase),
    )
    """Номер машины"""
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
    """Локация, в которой осуществляется подбор"""
    payload: Mapped[int]
    """Грузоподъемность"""
    location = relationship("Location", foreign_keys=[location_id])
    """Локация в которой находится машина"""

    @orm.validates("payload")
    def validate_payload(self, key, value):
        if not 1 < value <= 1000:
            raise ValueError(f"Invalid payload {value}")
        return value

    def to_read_model(self) -> MachineSchema:
        return MachineSchema(
            id=self.id,
            identifier=self.identifier,
            location=self.location.to_read_model(),
            payload=self.payload,
        )
