import pytest
from tempo.services.session import SessionService
from tempo.exceptions import SessionAlreadyActive, SessionNotFound


def test_start_activity(db_session):
    service = SessionService(db_session)

    session = service.start_activity("coding")
    assert session.activity == "coding"
    assert session.finished_at is None

def test_stop_activity(db_session):
    service = SessionService(db_session)

    service.start_activity("english")
    session = service.stop_activity()
    assert session.finished_at is not None

def test_cancel_activity(db_session):
    service = SessionService(db_session)

    service.start_activity("thing")

    service.cancel_activity()

    with pytest.raises(SessionNotFound):
        service.get_current_activity()

def test_current_status(db_session):
    service = SessionService(db_session)

    service.start_activity("coding")
    session = service.get_current_activity()

    assert session.activity == "coding"
    assert session.finished_at is None

    stopped_session = service.stop_activity()

    assert stopped_session.activity == "coding"
    assert stopped_session.finished_at is not None

def test_get_today(db_session):
    service = SessionService(db_session)

    assert len(service.get_today()) == 0

    service.start_activity("reading")
    service.stop_activity()

    service.start_activity("coding")

    today_sessions = service.get_today()
    assert len(today_sessions) == 2

    assert today_sessions[0].activity == "reading"
    assert today_sessions[0].finished_at is not None

    assert today_sessions[1].activity == "coding"
    assert today_sessions[1].finished_at is None

def test_stop_without_active_session(db_session):
    service = SessionService(db_session)

    with pytest.raises(SessionNotFound):
        service.stop_activity()

def test_status_without_active_session(db_session):
    service = SessionService(db_session)

    with pytest.raises(SessionNotFound):
        service.get_current_activity()

def test_start_with_active_session(db_session):
    service = SessionService(db_session)

    service.start_activity("activity")

    with pytest.raises(SessionAlreadyActive):
        service.start_activity("something")