from datetime import datetime, timedelta


bd, bc, be = 2000, 1, 1

birthday = datetime(bd, bc, be)


def add_gs(birthday: datetime) -> datetime:
    gs = timedelta(seconds=+ (10**9))
    return birthday + gs


print(add_gs(birthday))
