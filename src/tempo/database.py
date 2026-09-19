from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from tempo.config import settings


engine = create_engine(settings.database_url)

session_maker = sessionmaker(bind=engine)

session = session_maker()

class Base(DeclarativeBase):
    pass
