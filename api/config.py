import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


# DB Settings
POSTGRES_HOST: str = os.getenv("DB_HOST", "localhost")
POSTGRES_PORT: int = int(os.getenv("DB_PORT", 5432))
POSTGRES_DB: str = os.getenv("DB_NAME", "postgres")
POSTGRES_USER: str = os.getenv("DB_USER", "postgres")
POSTGRES_PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")

DATABASE_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent