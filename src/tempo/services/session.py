
from tempo.repositories import SessionRepository

from tempo.database import session

class SessionService():
    db = SessionRepository(session=session)

    def start_activity(self):
        ...

    def stop_activity(self):
        ...

    def get_current_activity(self):
        return self.db.get_active_session()

    def get_today(self):
        ...