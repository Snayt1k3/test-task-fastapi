import asyncio

from scripts.create_20_machines import create_20_machines
from scripts.update_locations_3min import update_locations
from scripts.uploading_locations import upload


async def main():
    await asyncio.sleep(30)  # ждем миграции
    await upload()
    await create_20_machines()
    await update_locations()


if __name__ == "__main__":
    asyncio.run(main())
