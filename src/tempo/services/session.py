
from tempo.repositories import SessionRepository

from tempo.database import session

class SessionService():
    db = SessionRepository(session=session)

    def get_current_activity(self):
        current_activity = self.db.get_active_session()
        if current_activity:
            return current_activity
        else:
            return Exception
        
    def start_activity(self, activity: str):
        created_session = self.db.create_session(activity)
        return created_session

    def stop_activity(self):
        ...

    

    def get_today(self):
        ...