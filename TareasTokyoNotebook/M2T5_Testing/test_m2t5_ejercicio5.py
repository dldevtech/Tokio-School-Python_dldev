from m2t5_ejercicio5 import filtrar_aprobados
import pytest

def test_mantener_orden():
    pares = [("Diego", 6), ("Cesaria", 8), ("Logan", 7)]
    esperado = ["Diego", "Cesaria", "Logan"]
    assert filtrar_aprobados(pares) == esperado

@pytest.mark.parametrize(
    "pares, esperado",
    [
        pytest.param([("Ana", 5)], ["Ana"], id ="caso_aprobado_unico"),
        pytest.param([("Ana", 5),("Luis", 7), ("Jose", 2)], ["Ana", "Luis"], id ="caso_mixto"),
        pytest.param([ ], [], id ="caso_vacio"),
        pytest.param([("Carlos", 3), ("Iván", 4), ("Sergio", 0)], [], id ="caso_suspensos")
    ]
)

def test_filtrar_aprobados(pares, esperado):
    assert filtrar_aprobados(pares) == esperado