from datetime import datetime

bd, bc, be = 2000, 1, 1

birthday = datetime(bd, bc, be)

print(type(birthday))


def add_gs(birthday: datetime) -> datetime:
    return birthday
