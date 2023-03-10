import simple_math
import pytest
'''
@pytest.mark.parametrize("a, b, expected", [
    (1,1,2),
    (2,3,5),
    (7,8,15),
    (24,12,36),
    (-5,5,0)])
        

def test_simple_add_oarametrized(a,b,expected):
    assert simple_math.simple_add(a,b) == expected
'''

'''
@pytest.mark.parametrize("a, b, expected", [
    (1,1,0),
    (2,3,-1),
    (7,8,-1),
    (24,12,12),
    (-5,5,-10)])


def test_simple_sub_parametrized(a,b,expected):
    assert simple_math.simple_sub(a,b) == expected
'''


@pytest.mark.parametrize("x, a0, a1,expected", [
    (3,2,1,5),
    (4,2,3,14)])

def test_simple_div_parametrized(x,a0,a1,expected):
    assert simple_math.poly_first(x,a0,a1) == expected

'''

@pytest.mark.parametrize("a, b, expected", [
    (1,1,2),
    (2,3,5),
    (7,8,15),
    (24,12,36),
    (-5,5,0)])
def test_simle_poly_first_parametrized(i1,i2, expected):
    assert simple_math.simple_poly_first(i1,i2) == expected


'''
'''
def test_simple_poly_second_parametrized(i1,i2, expected):
    assert simple_math.simple_poly_second(i1,i2, expected)
'''    
