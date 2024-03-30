from pydantic import BaseModel


class LocationSchema(BaseModel):
    id: int
    """Идентификатор в бд"""
    city: str
    """Город"""
    state: str
    """Штат, провинция, район"""
    zip: int
    """Почтовый индекс"""
    longitude: float
    """Долгота"""
    latitude: float
    """Широта"""


class LocationAddSchema(BaseModel):
    city: str
    """Город"""
    state: str
    """Штат, провинция, район"""
    zip: int
    """Почтовый индекс"""
    longitude: float
    """Долгота"""
    latitude: float
    """Широта"""
