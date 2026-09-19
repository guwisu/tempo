from sqlalchemy import select, scala

from src.tempo.models import SessionOrm


class SessionRepository():
    def __init__(self, session) -> None:
        self.model = SessionOrm
        self.session = self.session

    def get_active_session(self) -> SessionOrm | None:
        query = select(self.model).filter_by(finished_at=None)
        result = self.session.execute(query)
        model = result.scalars().one_or_none()
        if model is None:
            return None
        return model

    def create_session(self):
        ...

    def finish_session(self):
        ...

    def get_today_sessions(self):
        ...