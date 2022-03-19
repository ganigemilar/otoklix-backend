from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Database(BaseSettings):
    host: str
    name: str
    user: str
    password: str
