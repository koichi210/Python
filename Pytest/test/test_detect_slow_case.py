from main.detect_slow_case import Speed

def test_high_speed():

    assert Speed().high() == 'high speed'

def test_middle_speed():
    assert Speed().middle() == 'middle speed'

def test_low_speed():
    assert Speed().low() == 'low speed'
