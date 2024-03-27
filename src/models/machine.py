from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, CheckConstraint
from src.db.db import Base
from src.dto.machine import MachineSchema


class Machine(Base):
    __tablename__ = "machines"

    id: Mapped[int] = mapped_column(primary_key=True)
    """Идентификатор в бд"""
    identifier: Mapped[str]
    """Номер машины"""
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
    """Локация, в которой осуществляется подбор"""
    payload: Mapped[int] = mapped_column(Integer, CheckConstraint('payload > 1 AND payload < 1001'))
    """Грузоподъемность"""

    def to_read_model(self) -> MachineSchema:
        return MachineSchema(
            id=self.id,
            identifier=self.identifier,
            location_id=self.location_id,
            payload=self.payload
        )
