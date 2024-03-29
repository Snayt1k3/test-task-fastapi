from pydantic import BaseModel
from .location import LocationSchema
class MachineSchema(BaseModel):
    id: int
    """Идентификатор в бд"""
    identifier: str
    """Номер машины"""
    location: LocationSchema
    """Локация, в которой осуществляется подбор"""
    payload: int
    """Грузоподъемность"""
