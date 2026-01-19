from prime import primeno

def test_one():
    assert primeno(1) == "Not Prime"

def test_two():
    assert primeno(2) == "Prime"

def test_zero():
    assert primeno(0) == "Not Prime"
