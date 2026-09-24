

class SessionAlreadyExists(Exception):
    """Raised when active session is already exists"""
    pass


class SessionDoesNotExists(Exception):
    """Raised when session doesn't exists"""
    pass