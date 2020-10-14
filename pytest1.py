

# def funct(x):
#     return x+5
#
# def test_met1():
#     assert funct(3)==8
#
#
# funct(3)
import pytest
def fn(x,y):
    return x+y


def test_m2():
    assert fn(2,2)==4

print(fn(3,4))