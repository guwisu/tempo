
from tempo.repositories import SessionRepository

from tempo.database import session

class SessionService():
    db = SessionRepository(session=session)

    def get_current_activity(self):
        return self.db.get_active_session()

    def start_activity(self, activity: str):
        return self.db.create_session(activity)

    def stop_activity(self):
        return self.db.finish_session()

    def get_today(self):
        return self.db.get_today_sessions()
