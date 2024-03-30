import asyncio
import random

from src.dto.machine import MachineAddSchema
from src.utils.uow import UnitOfWork
from src.services.machines import MachinesService
from src.services.location import LocationService

async def create_20_machines():
    uow = UnitOfWork()
    service_loc = LocationService()
    service_mac = MachinesService()
    all_locations = await service_loc.get_locations(uow)

    for _ in range(20):
        location = random.choice(all_locations)
        machine = MachineAddSchema(payload=random.randint(1, 1000), zip=location.zip)
        await service_mac.add_machine(uow, machine)




if __name__ == "__main__":
    asyncio.run(create_20_machines())