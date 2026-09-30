from datetime import datetime, timezone, timedelta
from sqlalchemy import select, insert, update, delete

from tempo.models import SessionOrm


class SessionRepository():
    def __init__(self, session):
        self.model = SessionOrm
        self.session = session

    def get_active_session(self) -> SessionOrm | None:
        query = select(self.model).where(self.model.finished_at.is_(None))
        result = self.session.execute(query)
        return result.scalar_one_or_none()

    def create_session(self, activity: str) -> SessionOrm:
        stmt = insert(self.model).values(
            activity=activity.lower().strip(),
            started_at=datetime.now(timezone.utc),
            finished_at=None,
        ).returning(self.model)
        result = self.session.execute(stmt)
        model = result.scalar_one()
        self.session.commit()
        return model

    def finish_session(self) -> SessionOrm | None:
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

    def cancel_session(self) -> SessionOrm | None:
        stmt = (
            delete(self.model)
            .where(self.model.finished_at.is_(None))
            .returning(self.model)
        )
        result = self.session.execute(stmt)
        return result.scalar_one_or_none()
    
    def get_today_sessions(self) -> list[SessionOrm]:
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
        return result.scalars()
