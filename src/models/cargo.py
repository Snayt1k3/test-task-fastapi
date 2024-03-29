from sqlalchemy import ForeignKey, Integer, CheckConstraint, orm
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .location import Location
from src.db.db import Base
from src.dto.cargo import CargoSchema


class Cargo(Base):
    __tablename__ = "cargos"

    id: Mapped[int] = mapped_column(primary_key=True)
    """Идентификатор в бд"""
    pick_up_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
    """Локация, в которой осуществляется подбор"""
    delivery_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
    """Локация, в которую осуществляется доставка"""
    weight: Mapped[int] = mapped_column(Integer)
    """Вес груза"""
    description: Mapped[str]
    """Описание груза"""

    pick_up_location = relationship("Location", foreign_keys=[pick_up_id])
    delivery_location = relationship("Location", foreign_keys=[delivery_id])

    @orm.validates('weight')
    def validate_weight(self, key, value):
        if not 1 < value <= 1000:
            raise ValueError(f'Invalid weight {value}')
        return value

    def to_read_model(self) -> CargoSchema:
        return CargoSchema(
            id=self.id,
            pick_up_location=self.pick_up_location.to_read_model(),
            delivery_location=self.delivery_location.to_read_model(),
            weight=self.weight,
            description=self.description,

        )