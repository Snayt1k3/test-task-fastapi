from src.models.cargo import Cargo
from src.utils.repository import SQLAlchemyRepository
from sqlalchemy import select
from sqlalchemy.orm import joinedload

class CargosRepository(SQLAlchemyRepository):
    model = Cargo

    async def find_all(self):
        stmt = select(self.model).options(joinedload(self.model.pick_up_location), joinedload(self.model.delivery_location))
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by).options(joinedload(self.model.pick_up_location), joinedload(self.model.delivery_location))
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model()
        return res