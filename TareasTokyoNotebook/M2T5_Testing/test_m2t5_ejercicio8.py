from m2t5_ejercicio8 import media
import pytest

@pytest.mark.parametrize(
    "nums, esperado",
    [
        ([3,2,4,8], 4.25),
        ([3,3,2], 2.66),
    ]
)

def test_media_aprox(nums, esperado):
    assert media(nums) == pytest.approx(esperado, 0.01)

def test_lista_vacia():
    with pytest.raises(ValueError):
        media([])