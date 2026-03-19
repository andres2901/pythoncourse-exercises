import simple_math as sm
import pytest

@pytest.mark.parametrize("x, y, expected", [
(1, 1, 2),
(2, 2, 4),
(3, 3, 6)
])

def test_add(x, y, expected):
    assert sm.simple_add(x,y) == expected

@pytest.mark.parametrize("x, y, expected", [
(2, 1, 1),
(4, 2, 2),
(6, 3, 3)
])

def test_sub(x, y, expected):
   assert sm.simple_sub(x,y) == expected

def test_simple_mult():
    assert sm.simple_mult(1,1) == 1

def test_simple_div():
    assert sm.simple_div(1,1) == 1

def test_poly_first():
    assert sm.poly_first(1,1,1) == 2

def test_polysecond():
    assert sm.poly_second(1,1,1,1) == 3
