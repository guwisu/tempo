from tempo.repositories import SessionRepository
from tempo.exceptions import SessionAlreadyActive, SessionNotFound, InvalidActivityName
from tempo.schemas import Session

class SessionService():
    def __init__(self, session):
        self.db = SessionRepository(session=session)

    def get_current_activity(self):
        current_activity = self.db.get_active_session()
        if current_activity is None:
            raise SessionNotFound("Activity session not found!")
        return Session.model_validate(current_activity)

    def start_activity(self, activity: str):
        test_activity = self.db.get_active_session()
        if test_activity:
            raise SessionAlreadyActive("Activity session already active!")
        clear_activity = activity.strip()
        if not clear_activity:
            raise InvalidActivityName("Activity name can't be empty!")
        if len(clear_activity) > 100:
            raise InvalidActivityName("Activity name is too long (max 100 chars)!")
        
        new_activity = self.db.create_session(activity)
        result = Session.model_validate(new_activity)
        self.db.session.commit()
        return result

    def stop_activity(self):
        stopped_activity = self.db.finish_session()
        if not stopped_activity:
            raise SessionNotFound("Activity session not found!")
        result = Session.model_validate(stopped_activity)
        self.db.session.commit()
        return result

    def cancel_activity(self):
        canceled_activity = self.db.cancel_session()
        if not canceled_activity:
            raise SessionNotFound("Activity session not found!")
        result = Session.model_validate(canceled_activity)
        self.db.session.commit()
        return result

    def get_today(self):
        return list(map(Session.model_validate, self.db.get_today_sessions()))
