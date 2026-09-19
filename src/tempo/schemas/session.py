from pydantic import BaseModel

from datetime import datetime

class Session(BaseModel):
    id: int
    activity: str
    started_at: datetime
    finished_at: datetime | None