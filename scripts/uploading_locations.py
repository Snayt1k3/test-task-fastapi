import asyncio
import csv
from src.utils.uow import UnitOfWork
from src.dto.location import LocationAddSchema
from src.services.location import LocationService


async def upload():
    service = LocationService()
    uow = UnitOfWork()

    with open("uszips.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for i, row in enumerate(csvreader):
            if i == 0:
                continue

            location = LocationAddSchema(
                city=row[3],
                state=row[5],
                zip=int(row[0]),
                longitude=float(row[2]),
                latitude=float(row[1]),
            )

            await service.add_location(uow, location)


if __name__ == "__main__":
    asyncio.run(upload())
