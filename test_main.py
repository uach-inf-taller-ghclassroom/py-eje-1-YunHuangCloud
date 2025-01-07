from main import *

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(101, 322) == 423
    assert sumar(0, 7) == 7
    assert sumar(-1, -2) == -3
    assert sumar(-9, 13) == 4

# Otra forma:
# import pytest
# def test_sumar():
#     with pytest.raises(TypeError):
#         assert func(3) == 5, "value must be 5"

