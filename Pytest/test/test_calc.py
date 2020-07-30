from main.calc import Calc

def test_add_01():
    assert Calc(9, 2).add() == 11

def test_add_02():
    assert Calc(-9, 2).add() == -7

def test_sub_01():
    assert Calc(9, 2).sub() == 7

def test_sub_02():
    assert Calc(-9, 2).sub() == -11

def test_multiple_01():
    assert Calc(9, 2).multiple() == 18

def test_multiple_02():
    assert Calc(-9, 2).multiple() == -18

def test_multiple_03():
    assert Calc(-9, -2).multiple() == -18   # expect assert 

def test_divide_01():
    assert Calc(9, 2).divide() == 4.5

def test_divide_02():
    assert Calc(-9, 2).divide() == -4.5

