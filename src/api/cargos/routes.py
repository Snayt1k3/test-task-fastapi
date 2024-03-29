from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.api.deps import UOWDep
from src.dto.cargo import CargoSchemaAdd, CargoSchemaFilter, CargoSchemaEdit
from src.services.cargo import CargosService


cargos_router = APIRouter(prefix="cargo", tags=["cargo"])


@cargos_router.post(path="/")
async def create_cargo(uow: UOWDep, cargo: CargoSchemaAdd):
    cargo_id = await CargosService().add_cargo(uow, cargo)
    return JSONResponse(cargo_id)


@cargos_router.get(path="/list")
async def get_cargos(uow: UOWDep, filter: CargoSchemaFilter):
    cargos = await CargosService().get_cargos_with_machines(uow, filter)
    return JSONResponse(cargos)


@cargos_router.get("/{id}")
async def get_cargo(uow: UOWDep, id: int):
    cargo = await CargosService().get_cargo_and_machines(uow, id)
    return JSONResponse(cargo)


@cargos_router.delete("/{id}")
async def get_cargo(uow: UOWDep, id: int):
    cargo = await CargosService().delete_cargo(uow, id)
    return JSONResponse(cargo)


@cargos_router.patch("/")
async def get_cargo(uow: UOWDep, cargo: CargoSchemaEdit):
    cargo = await CargosService().edit_cargo(uow, cargo)
    return JSONResponse(cargo)
