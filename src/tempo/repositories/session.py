from datetime import datetime, timezone, timedelta
from sqlalchemy import select, insert, update

from tempo.models import SessionOrm
from tempo.schemas import Session
from tempo.exceptions import SessionAlreadyExists


class SessionRepository():
    def __init__(self, session) -> None:
        self.session = session
        self.model = SessionOrm

    def get_active_session(self) -> Session | None:
        query = select(self.model).where(self.model.finished_at.is_(None))
        result = self.session.execute(query)
        return result.scalars().one_or_none()

    def create_session(self, activity: str):
        test_query = select(self.model).where(self.model.finished_at.is_(None))
        test_result = self.session.execute(test_query)
        if test_result.scalars().one_or_none() is not None:
            raise SessionAlreadyExists("Active session already exists!")
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
        model = result.scalar_one_or_none()
        self.session.commit()
        return model


    def get_today_sessions(self):
        today_start = datetime.now(timezone.utc).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        today_end = today_start + timedelta(days=1)
        query = (
            select(self.model)
            .where(self.model.started_at >= today_start)
            .where(self.model.started_at < today_end)
            .order_by(self.model.started_at)
        )
        result = self.session.execute(query)
        return result.scalars().all()
