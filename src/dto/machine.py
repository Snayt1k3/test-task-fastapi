from pydantic import BaseModel

class MachineSchema(BaseModel):
    id: int
    """Идентификатор в бд"""
    identifier: str
    """Номер машины"""
    location_id: int
    """Локация, в которой осуществляется подбор"""
    payload: int
    """Грузоподъемность"""
