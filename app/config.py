from pydantic import BaseSettings
from os import path

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str


    class Config:
        env_file = f"{path.dirname(path.abspath(__file__))}/../.env"



settings = Settings()