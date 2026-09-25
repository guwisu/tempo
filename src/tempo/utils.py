from datetime import datetime, timedelta


def _format_duration(td: timedelta) -> str:
    """Format a timedelta as Xh Ym Zs."""
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    parts = []
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    parts.append(f"{seconds}s")
    return " ".join(parts)

def _format_time(dt: datetime) -> str:
    """Format UTC datetime to local time string (HH:MM:SS)"""
    local_dt = dt.astimezone()
    return local_dt.strftime("%H:%M:%S")