import pytest
from m2t5_ejercicio1 import sumatoria_positivos

def test_Sumatoria_listas_vacias():
    assert sumatoria_positivos([]) == 0

def test_sumatoria_negativos():
    assert sumatoria_positivos([-5,-6,-4]) == 0

def test_sumatoria_mixtos():
    assert sumatoria_positivos([-5, 5, 6]) == 11

def test_sumatoria_positivos():
    assert sumatoria_positivos([3, 2, 5]) == 10

@pytest.mark.parametrize(
    "nums, esperado",
    [
        ([], 0),
        ([-5,-6,-4], 0),
        ([-5, 5, 6], 11),
        ([3, 2, 5], 10),
        ([6, 3, 1, -10, 100], 110)
        
    ]
)
def test_sumatoria_parametrizada(nums, esperado):
    assert sumatoria_positivos(nums) is esperado