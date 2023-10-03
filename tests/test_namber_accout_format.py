from src.funtion import namber_accout_format

c = "Maestro 7552745726849311"
a = "Счет 34799481846914116850"


def test_namber_accout_format():
    assert namber_accout_format(c) == "Maestro 7552 74** **** 9311"
    assert namber_accout_format(a) == "Счет **6850"
    assert namber_accout_format("") == None
   