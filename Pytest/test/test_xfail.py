from main.calc import Calc
import pytest

def test_multiple_01():
    assert Calc(9, 2).multiple() == 18

def test_multiple_02():
    assert Calc(9, 2).multiple() == -18

@pytest.mark.xfail
def test_multiple_03():
    assert Calc(9, 2).multiple() == -18   # expect assert 

@pytest.mark.xfail
def test_multiple_04():
    assert Calc(9, 2).multiple() == 18   # expect assert 
