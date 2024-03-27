from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.dto.location import LocationSchema


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    """Идентификатор в бд"""
    city: Mapped[str]
    """Город"""
    state: Mapped[str]
    """Штат, провинция, район"""
    zip: Mapped[int]
    """Почтовый индекс"""
    longitude: Mapped[float]
    """Долгота"""
    latitude: Mapped[float]
    """Широта"""

    def to_read_model(self) -> LocationSchema:
        return LocationSchema(
            id=self.id,
            city=self.city,
            state=self.state,
            zip=self.zip,
            latitude=self.latitude,
            longitude=self.longitude,
        )
