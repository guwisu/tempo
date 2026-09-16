from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from src.tempo.config import settings


engine = create_engine(settings.database_url)

session_maker = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
