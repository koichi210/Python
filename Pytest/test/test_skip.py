from main.greeting import English,Spanish
import pytest

def test_English_greeting1():
    assert English().greeting1() == 'Hello'

@pytest.mark.skip(reason='T.B.D')
def test_English_greeting2():
    assert English().greeting2() == 'Bye'

def test_English_greeting3():
    assert English().greeting2() == 'Riposo'  # expect assert
