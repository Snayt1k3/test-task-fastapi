from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.dto.machine import MachineEditSchema
from src.services.machines import MachinesService
from src.api.deps import UOWDep

machines_router = APIRouter(prefix="/machine", tags=["Machine"])


@machines_router.patch("/")
async def edit_machine(uow: UOWDep, machine: MachineEditSchema):
    machine = await MachinesService().edit_machine(uow, machine)
    return JSONResponse(machine)
