from scripts.gigasecond import *


def test_add_gs_returns_input_date():
    bd = datetime(2000, 1, 1)
    assert add_gs(bd) == datetime(2031, 9, 9, 1, 46, 40)
