from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    MODE: Literal['DEV', 'TEST', 'PROD']

    DB_USER: str
    DB_PASS: str
    DB_PORT: str
    DB_HOST: str
    DB_NAME: str

    DB_TEST_USER: str
    DB_TEST_PASS: str
    DB_TEST_HOST: str
    DB_TEST_PORT: str
    DB_TEST_NAME: str

    SECRET: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    


    @property
    def database_test_url(self):
        return f"postgresql+asyncpg://{self.DB_TEST_USER}:{self.DB_TEST_PASS}@{self.DB_TEST_HOST}:{self.DB_TEST_PORT}/{self.DB_TEST_NAME}"

settings = Settings()