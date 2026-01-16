# test_cube.py

from cube import cube

def test_cube_positive():
    assert cube(3) == 27

def test_cube_zero():
    assert cube(0) == 0

def test_cube_negative():
    assert cube(-2) == -8
