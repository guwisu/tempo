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
            activity=activity,
            started_at=datetime.now(timezone.utc),
            finished_at=None,
        ).returning(self.model)
        result = self.session.execute(stmt)
        model = result.scalar_one()
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
        local_now = datetime.now().astimezone()
        local_today_start = local_now.replace(hour=0, minute=0, second=0, microsecond=0)

        utc_today_start = local_today_start.astimezone(timezone.utc)
        uts_today_end = utc_today_start + timedelta(days=1)
        
        query = (
            select(self.model)
            .where(self.model.started_at >= utc_today_start)
            .where(self.model.started_at < uts_today_end)
            .order_by(self.model.started_at)
        )
        result = self.session.execute(query)
        return list(result.scalars())
