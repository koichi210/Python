import pytest
from main.calc import Calc

class TestMyModule:
    @pytest.mark.parametrize(
        "x, y, expect", [
        (1, 2, 3),
        (3, 4, 7),
        (5, 6, 11),
        (5, 6, 15)
    ])

    @pytest.mark.usefixtures('promise')
    def test_01(self, x, y, expect):
        assert Calc(x, y).add() == expect
