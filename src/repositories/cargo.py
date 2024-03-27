from src.models.cargo import Cargo
from src.utils.repository import SQLAlchemyRepository


class CargosRepository(SQLAlchemyRepository):
    model = Cargo
