from src.funtion import filtr_exequted

m = [{"state": "EXECUTED"}, {"state": "CANCELED"}]


def test_filtr_exequted():
    assert filtr_exequted(m) == [{"state": "EXECUTED"}]
