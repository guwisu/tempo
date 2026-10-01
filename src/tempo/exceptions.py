

class SessionAlreadyActive(Exception):
    """Raised when active session is already exists"""
    pass


class SessionNotFound(Exception):
    """Raised when session doesn't exists"""
    pass


class InvalidActivityName(Exception):
    """Raised when activity name is empty or too long"""
    pass