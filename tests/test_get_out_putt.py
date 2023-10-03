from src.funtion import get_out_putt

f = {
    "id": 121646999,
    "state": "CANCELED",
    "date": "2018-06-08T16:14:59.936274",
    "operationAmount": {
        "amount": "91121.62",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 7552745726849311",
    "to": "Счет 34799481846914116850"
}


def test_get_out_putt():
    assert get_out_putt(
        f) == f"08.06.2018 Перевод организации\nMaestro 7552 74** **** 9311 -> Счет **6850\n91121.62 руб."
