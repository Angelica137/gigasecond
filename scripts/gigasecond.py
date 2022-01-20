from datetime import datetime, timedelta

bd, bc, be = 2000, 1, 1

birthday = datetime(bd, bc, be)
gs = timedelta(seconds=+1)


def add_gs(birthday: datetime) -> datetime:
    return birthday


print(birthday)
print(gs)
print(birthday + gs)
