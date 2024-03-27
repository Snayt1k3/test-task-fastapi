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
    longitude: int
    """Долгота"""
    latitude: int
    """Широта"""
