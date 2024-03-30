import asyncio
import logging
import random

from src.dto.machine import MachineEditSchema
from src.utils.uow import UnitOfWork
from src.services.machines import MachinesService
from src.services.location import LocationService

logger = logging.getLogger(__name__)


async def update_locations():
    uow = UnitOfWork()
    service_loc = LocationService()
    service_mac = MachinesService()
    time = 60 * 3  # 3 минуты

    while True:
        logger.info("start update machine locations")
        all_locations = await service_loc.get_locations(uow)
        all_machines = await service_mac.get_machines(uow)

        for machine in all_machines:
            location = random.choice(all_locations)
            machine = MachineEditSchema(id=machine.id, zip=location.zip)
            await service_mac.edit_machine(uow, machine)

        logger.info("locations update was done")
        await asyncio.sleep(time)
