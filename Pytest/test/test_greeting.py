from main.greeting import English,Spanish

def test_English_greeting1():
    assert English().greeting1() == 'Hello'

def test_English_greeting2():
    assert English().greeting2() == 'Bye'

def test_English_greeting3():
    assert English().greeting2() == 'Riposo'  # expect assert

def test_Spanish_greeting1():
    assert Spanish().greeting1() == 'Hola'

def test_Spanish_greeting2():
    assert Spanish().greeting2()== 'Chao'
