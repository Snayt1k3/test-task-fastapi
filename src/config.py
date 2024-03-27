import os


class Config:
    DATABASE_URI: str = None


def load_config() -> Config:
    return Config()

