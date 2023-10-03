from src.funtion import get_operatios_list
import os


def test_get_operatios_list():
    dir_ = os.path.dirname(__file__)
    file_path = os.path.join(dir_, 'test.json')
    assert get_operatios_list(file_path) == [1, 2, 3]
