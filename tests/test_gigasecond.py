from scripts.gigasecond import *


def test_date_returns_input_date():
    bd = (2000, 1, 1)
    assert add_gs(bd) == (2000, 1, 1)