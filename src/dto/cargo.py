from pydantic import BaseModel


class CargoSchema(BaseModel):
    id: int
    """Идентификатор в бд"""
    pick_up_id: int
    """Id Локации, в которой осуществляется подбор"""
    delivery_id: int
    """Id Локации, в которую осуществляется доставка"""
    weight: int
    """Вес груза"""
    description: str
    """Описание груза"""


class CargoSchemaAdd(BaseModel):
    weight: int
    """Вес груза"""
    description: str
    """Описание груза"""
    pick_up_zip: int
    """Zip код pick_up локации"""
    delivery_zip: int
    """Zip код доставки"""


class CargoSchemaFilter(BaseModel):
    weight: int = None
    """Вес груза"""
    miles: int = None
    """Максимальное расстояние от машины до груза"""


class CargoSchemaEdit(BaseModel):
    id: int
    """Идентификатор в бд"""
    weight: int = None
    """Вес груза"""
    description: str = None
    """Описание груза"""
