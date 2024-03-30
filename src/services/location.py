from src.dto.location import LocationAddSchema
from src.utils.uow import IUnitOfWork
class LocationService:
    async def add_location(self, uow: IUnitOfWork, location: LocationAddSchema):
        location = location.model_dump()
        async with uow:
            id = await uow.locations.add_one(location)
            await uow.commit()

            return id