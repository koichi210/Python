from main.calc import Calc
import pytest

def test_divide_01():
    assert Calc(6, 2).divide() == 3

def test_divide_02():
    with pytest.raises(ZeroDivisionError):
        # 例外を期待し、例外が発生する
        Calc(4, 0).divide()

def test_divide_03():
    with pytest.raises(ZeroDivisionError):
        # 例外を期待しているが、例外発生しない
        Calc(4, 2).divide()
