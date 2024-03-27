from abc import ABC, abstractmethod
from typing import Type

from src.db.db import async_session_maker
from src.repositories.location import LocationsRepository
from src.repositories.machine import MachinesRepository
from src.repositories.cargo import CargosRepository

class IUnitOfWork(ABC):
    cargos: Type[CargosRepository]
    machines: Type[MachinesRepository]
    locations: Type[LocationsRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.machines = MachinesRepository(self.session)
        self.locations = LocationsRepository(self.session)
        self.cargos = CargosRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()