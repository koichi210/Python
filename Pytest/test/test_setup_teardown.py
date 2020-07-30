from main.greeting import English,Spanish
import pytest

def test_English_greeting1():
    assert English().greeting1() == 'Hello'

def test_English_greeting2():
    assert English().greeting2() == 'Bye'
