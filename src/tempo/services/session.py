
from tempo.repositories import SessionRepository

from tempo.database import session

class SessionService():
    db = SessionRepository(session=session)

    def start_activity(self):
        ...

    def stop_activity(self):
        ...

    def get_current_activity(self):
        current_activity = self.db.get_active_session()
        if current_activity:
            return current_activity
        else:
            return Exception

    def get_today(self):
        ...