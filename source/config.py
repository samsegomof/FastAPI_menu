import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME: str = os.getenv('PROJECT_NAME')
VERSION: str = '1.0'

PG_HOST: str = os.getenv('DB_HOST', 'localhost')
PG_PORT: int = int(os.getenv('DB_PORT', 5432))
PG_NAME: str = os.getenv('DB_NAME', 'postgres')
PG_USER: str = os.getenv('DB_USER', 'postgres')
PG_PASSWORD: str = os.getenv('DB_PASSWORD', 'postgres')

DB_URL: str = f'postgresql+asyncpg://test:test@localhost:5432/test'

BASE_DIR = Path(__file__).resolve().parent.parent
