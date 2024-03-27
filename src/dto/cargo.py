from pydantic import BaseModel

class CargoSchema(BaseModel):
    id: int
    """Идентификатор в бд"""
    pick_up_id: int
    """Локация, в которой осуществляется подбор"""
    delivery_id: int
    """Локация, в которую осуществляется доставка"""
    weight: int
    """Вес груза"""
    description: str
    """Описание груза"""
