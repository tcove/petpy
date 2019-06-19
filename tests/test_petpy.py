from petpy import gardner
from petpy import impedance


EPSILON = 1e-6 # global

def test_gardner():
    rhob = gardner(2000)    # 2073
    assert abs(rhob - 2073.0949454) < EPSILON

def test_impedance():
    ai = impedance(2000, 2500)
    assert abs(ai - 5000000) < EPSILON
