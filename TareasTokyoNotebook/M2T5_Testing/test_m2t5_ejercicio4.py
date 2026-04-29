from m2t5_ejercicio4 import contar_palabras
import pytest

@pytest.mark.parametrize(
    "texto, diccionario",
    [
        pytest.param("", {}, id="cadena_vacia"),
        pytest.param("Eco eco eco", {"eco":3}, id="cadena_palabras_repetidas"),
        pytest.param("Hola hola", {"hola":2}, id="cadena_Hola_hola"), 
    ],
)
def test_contar_palabras(texto, diccionario):
    assert contar_palabras(texto) == diccionario