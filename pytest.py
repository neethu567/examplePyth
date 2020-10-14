import pytest
@pytest.fixture
def function():
    x=30



    return x
def test_met(function):
    assert function % 3==0

def test_met2(function):
    assert function %6 ==0