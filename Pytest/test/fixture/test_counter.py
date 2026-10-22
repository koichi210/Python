from main.counter import Counter

def test_add_01():
    assert Counter().Increment() == 1

def test_add_02():
    counter = Counter()
    assert counter.Increment() == 1
    assert counter.Decrement() == 0

def test_add_03():
    assert Counter().Decrement() == -1
