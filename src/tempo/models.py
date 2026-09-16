from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String, DateTime
from datetime import datetime

from src.tempo.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    activity: Mapped[str] = mapped_column(String(100), nullable=False)
    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
    )    
    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
