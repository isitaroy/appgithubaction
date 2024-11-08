from src.maths_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(7,3) == 10
    assert add(-1,1) == 0

def test_sub():
    assert sub(6,3) == 3
    assert sub(2,3) == -1
    assert sub(9,3) == 6