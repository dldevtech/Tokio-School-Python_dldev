from m2t5_ejercicio3 import maximo_seguro
import pytest

def test_numeros_enteros():
    assert maximo_seguro([3,5,2,10]) == 10

def test_numeros_float():
    assert maximo_seguro([2.0,5.0,100.0]) == 100.0

def test_lista_vacia():
    with pytest.raises(ValueError):
        maximo_seguro([])