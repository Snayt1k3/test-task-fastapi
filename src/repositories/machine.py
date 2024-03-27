from src.models.machine import Machine
from src.utils.repository import SQLAlchemyRepository


class MachinesRepository(SQLAlchemyRepository):
    model = Machine
