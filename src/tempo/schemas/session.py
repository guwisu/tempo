from pydantic import BaseModel, ConfigDict

from datetime import datetime

class Session(BaseModel):
    id: int
    activity: str
    started_at: datetime
    finished_at: datetime | None

    model_config = ConfigDict(from_attributes=True)