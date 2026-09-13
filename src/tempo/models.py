from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, date

from src.tempo.database import Base


class Session(Base):
    __tablename__ = "Sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    activity: Mapped[str]
    started_at: Mapped[datetime]
    finished_at: Mapped[datetime]
