import os
from os import path
from platform import system
from typing import Optional, List, ClassVar # 수정

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BASE_DIR: str = path.dirname((path.abspath(__file__)))
    LOCAL_MODE: bool = True if system().lower().startswith("darwin") or system().lower().startswith("Windows") else False
    app_name: str = "Imizi API"
    TEST_MODE: bool = False

    ALLOW_SITE: List[str] = ["*"]
    TRUSTED_HOSTS: List[str] = ["*"]
    JWT_ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: Optional[str] = os.getenv("JWT_SECRET", "imizi-secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1  # one day
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 60  # sixty day

    DB_URL: Optional[str] = ""
    DB_POOL_RECYCLE: Optional[int] = 900
    DB_ECHO: Optional[bool] = True
    DB_POOL_SIZE: Optional[int] = 1
    DB_MAX_OVERFLOW: Optional[int] = 1

    AWS_REGION: Optional[str] = "us-west-1"
    AWS_BUCKET_NAME: Optional[str] = "mj-fastapi-imizi-1"
    AWS_ACCESS_KEY: Optional[str] = os.getenv("AWS_ACCESS_KEY", "")
    AWS_SECRET_KEY: Optional[str] = os.getenv("AWS_SECRET_KEY", "")

class DevSettings(Settings):
    DB_URL: str = f"mysql+pymysql://{os.getenv('DB_INFO')}/imizi?charset=utf8mb4"
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10

class TestSettings(Settings):
    DB_URL: str = "mysql+pymysql://root:Yys900105?@localhost:3306/imizi?charset=utf8mb4"
    DB_POOL_SIZE: int  = 1
    DB_MAX_OVERFLOW: int  = 0

class ProdSettings(Settings):
    DB_URL: str = "mysql+pymysql://root:Yys900105?@localhost:3306/imizi?charset=utf8mb4"
    DB_POOL_SIZE: int  = 5
    DB_MAX_OVERFLOW: int  = 10

def get_env():
    cfg_cls = dict(
        prd=ProdSettings,
        dev=DevSettings,
        test=TestSettings,
    )
    env = cfg_cls[os.getenv("FASTAPI_ENV", "dev")]()

    return env

settings = get_env()