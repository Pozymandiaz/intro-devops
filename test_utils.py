# test_utils.py
from test_utils import calculate_average

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([]) == 0
    assert calculate_average([10, 20, 30]) == 20.0
