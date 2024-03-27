from src.models.location import Location
from src.utils.repository import SQLAlchemyRepository


class LocationsRepository(SQLAlchemyRepository):
    model = Location
