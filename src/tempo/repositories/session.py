from datetime import datetime, timezone
from sqlalchemy import select, insert

from tempo.models import SessionOrm
from tempo.schemas import Session

class SessionRepository():
    def __init__(self, session) -> None:
        self.session = session
        self.model = SessionOrm

    def get_active_session(self) -> Session | None:
        query = select(self.model).filter_by(finished_at=None)
        result = self.session.execute(query)
        model = result.scalars().one_or_none()
        if model is None:
            return None
        return model

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
        ...

    def get_today_sessions(self):
        ...