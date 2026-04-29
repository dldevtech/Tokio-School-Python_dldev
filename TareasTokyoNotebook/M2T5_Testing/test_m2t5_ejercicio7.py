from m2t5_ejercicio7 import factorial
import pytest

@pytest.mark.parametrize(
    "n, esperado",
    [
        (0, 1),
        (1, 1),
        (5, 120),
    ]
)
def test_factorial_parametrizado(n, esperado):
    assert factorial(n) == esperado

def test_num_negativo():
    with pytest.raises(ValueError):
        factorial(-1)
