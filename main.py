import logging
from fastapi import FastAPI
from src.api.routers import all_routers
import uvicorn
from src.config import load_config

config = load_config()

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format=(
        "%(asctime)s - %(filename)s - %(levelname)s - "
        "%(name)s - %(funcName)s: %(lineno)d - %(message)s"
    ),
    datefmt="%m/%d/%Y %I:%M:%S %p %Z",
)

app = FastAPI(title="App")

for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
