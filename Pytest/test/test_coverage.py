from main.comp import Comp
import pytest

def test_add_01():
    assert Comp().compare(1, 2) == -1

def test_add_02():
    assert Comp().compare(2, 2) == 0

@pytest.mark.skip(reason='coverage test')
def test_add_03():
    assert Comp().compare(2, 1) == 1
