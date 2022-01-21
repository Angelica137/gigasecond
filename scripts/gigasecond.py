from datetime import datetime, timedelta


def add_gs(birthday: datetime) -> datetime:
    gs = timedelta(seconds=+ (10**9))
    return birthday + gs
