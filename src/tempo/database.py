from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from tempo.config import settings


engine = create_engine(settings.database_url)

session_maker = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


@contextmanager
def get_session():
    with session_maker() as session:
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
