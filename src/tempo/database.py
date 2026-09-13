from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from src.tempo.config import settings


engine = create_engine(settings.DB_URL)

session_maker = sessionmaker(bind=engine)

session = session_maker()

class Base(DeclarativeBase):
    pass
