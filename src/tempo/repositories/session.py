from datetime import datetime, timezone
from sqlalchemy import select, insert, update

from tempo.models import SessionOrm
from tempo.schemas import Session

class SessionRepository():
    def __init__(self, session) -> None:
        self.session = session
        self.model = SessionOrm

    def get_active_session(self) -> Session | None:
        query = select(self.model).where(self.model.finished_at.is_(None))
        result = self.session.execute(query)
        return result.scalars().one_or_none()

    def create_session(self, activity: str):
        stmt = insert(self.model).values(
            activity=activity,
            started_at=datetime.now(timezone.utc),
            finished_at=None,
        ).returning(self.model)
        result = self.session.execute(stmt)
        model = result.scalar_one()
        self.session.commit()
        return model

    def finish_session(self):
        stmt = (
            update(self.model)
            .values(finished_at=datetime.now(timezone.utc))
            .where(self.model.finished_at.is_(None))
            .returning(self.model)
        )
        result = self.session.execute(stmt)
        model = result.scalar_one()
        self.session.commit()
        return model


    def get_today_sessions(self):
        ...