from sqlalchemy import select

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
        return model.activity

    def create_session(self):
        ...

    def finish_session(self):
        ...

    def get_today_sessions(self):
        ...