import pytest
from m2t5_ejercicio2 import es_palindromo

@pytest.mark.parametrize(
    "p, esperado",
    [
        pytest.param("", True, id="cadena_vacia"),
        pytest.param("radar", True, id="palabra_minus_palindroma"),
        pytest.param("Radar", True, id="palabra_mayus_palindroma"),
        pytest.param("SomOs", True, id="palabra_mixta_palindroma"),
        pytest.param("Amor a Roma", True, id="frase_palíndroma"),
        pytest.param("No soy palíndromo", False, id="frase_no_palíndroma"),
        pytest.param("33", True, id="numero_palindromo"),
        pytest.param("34", False, id="numero_no_palindromo"),
        
    ],
)
def test_es_palindromo(p, esperado):
    assert es_palindromo(p) is esperado