from geopy.distance import geodesic

from src.dto.cargo import (
    CargoSchemaAdd,
    CargoSchemaEdit,
    CargoSchema,
    CargoSchemaFilter,
)
from src.utils.uow import IUnitOfWork


class CargosService:
    async def add_cargo(self, uow: IUnitOfWork, cargo: CargoSchemaAdd) -> int:
        """Добавляет Груз в БД"""
        async with uow:
            pick_location = await uow.locations.find_one(zip=cargo.pick_up_zip)
            delivery_location = await uow.locations.find_one(zip=cargo.pick_up_zip)

            cargo_id = await uow.cargos.add_one(
                {
                    "delivery_id": delivery_location.id,
                    "pick_up_id": pick_location.id,
                    "weight": cargo.weight,
                    "description": cargo.description,
                }
            )
            await uow.commit()
            return cargo_id

    async def get_cargos_with_machines(
        self, uow: IUnitOfWork, filter: CargoSchemaFilter
    ):
        """Получение всех грузов и ближайших машин к ним"""

        r_dict = {"cargos": []}

        async with uow:
            all_cargos = [
                cargo
                for cargo in await uow.cargos.find_all()
                if filter.weight is None or cargo.weight == filter.weight
            ]
            all_machines = await uow.machines.find_all()

            for cargo in all_cargos:
                pick_up_location = await uow.locations.find_one(id=cargo.pick_up_id)
                r_dict["cargos"].append(
                    {
                        "cargo": cargo.model_dump(),
                        "nearest_cars": len(
                            [
                                machine
                                for machine in all_machines
                                if geodesic(
                                    (
                                        machine.location.latitude,
                                        machine.location.longitude,
                                    ),
                                    (
                                        pick_up_location.latitude,
                                        pick_up_location.longitude,
                                    ),
                                ).miles
                                <= filter.miles
                            ]
                        ),
                    }
                )
        return r_dict

    async def get_cargo_and_machines(self, uow: IUnitOfWork, id: int):
        """Получает груз из бд по и все машины с расстоянием"""
        r_dict = {"machines": []}
        async with uow:
            cargo: CargoSchema = await uow.cargos.find_one(id=id)
            all_machines = await uow.machines.find_all()

            for machine in all_machines:
                pick_up_location = await uow.locations.find_one(id=cargo.pick_up_id)

                r_dict["machines"].append(
                    {
                        "car_number": machine.identifier,
                        "distance": geodesic(
                            (machine.location.latitude, machine.location.longitude),
                            (
                                pick_up_location.latitude,
                                pick_up_location.longitude,
                            ),
                        ).miles,
                    }
                )
            r_dict.update(cargo.model_dump())
        return r_dict

    async def edit_cargo(self, uow: IUnitOfWork, cargo: CargoSchemaEdit):
        """Обновляет груз в бд"""
        async with uow:
            id = await uow.cargos.edit_one(
                cargo.id, {"description": cargo.description, "weight": cargo.weight}
            )
            await uow.commit()
            return id

    async def delete_cargo(self, uow: IUnitOfWork, id: int):
        """Удаляет груз из бд"""
        async with uow:
            cargo_id = await uow.cargos.delete_one(id)
            await uow.commit()
            return cargo_id
