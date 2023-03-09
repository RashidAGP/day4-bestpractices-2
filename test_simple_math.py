import simple_math
import pytest

@pytest.mark.parametrized("i1, i2, expected", [
    (1,1,2),
    (2,3,5),
    (7,8,15),
    (2,10,12)])

def test_simple_add_oarametrized(i1,i2,expected):
    assert simple_math.simple_add(i1,i2) == expected

def test_simple_sub_parametrized(i1,i2,expected):
    assert simple_math.simple_sub(i1,i2) == expected

def test_simple_div_parametrized(i1,i2,expected):
    assert simple_math.simple_div(i1,i2) == expected

def test_simle_poly_first_parametrized(i1,i2, expected):
    assert simple_math.simple_poly_first(i1,i2) == expected

def test_simple_poly_second_parametrized(i1,i2, expected):
    assert simple_math.simple_poly_second(i1,i2, expected):
    
