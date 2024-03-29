from src.utils.uow import IUnitOfWork
from src.dto.machine import MachineEditSchema


class MachinesService:

    async def edit_machine(self, uow: IUnitOfWork, machine: MachineEditSchema):
        async with uow:
            location = await uow.locations.find_one(zip=machine.zip)
            id = await uow.machines.edit_one(
                id=machine.id, data={"location_id": location.id}
            )

            await uow.commit()

            return id
