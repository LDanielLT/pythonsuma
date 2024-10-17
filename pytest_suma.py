import pytest
from suma import suma

def test_sumar_positivos():
    assert suma(1, 2) == 3
    assert suma(10, 5) == 15
    assert suma(-1, -1) == -2
    assert suma(-5, 3) == -2
def test_suma2():
    assert suma(0, 0) == 0
    assert suma(0, 5) == 5
    assert suma(" " , 0) == "error"
    assert suma("l",0) == "error"
