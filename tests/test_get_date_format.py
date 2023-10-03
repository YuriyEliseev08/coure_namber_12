from src.funtion import get_date_format

d = "2018-06-24T00:46:32.422648"


def test_get_date_format():
    assert get_date_format(d) == "24.06.2018"
   