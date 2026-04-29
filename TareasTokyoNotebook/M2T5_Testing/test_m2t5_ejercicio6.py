from m2t5_ejercicio6 import normalizar_email
import pytest

@pytest.mark.parametrize(
    "email, esperado",
    [
        pytest.param("miemail@yaju.com", ("miemail","yaju.com"), id="caso_valido"),
        pytest.param("MIEMAIl@guguel.es", ("miemail","guguel.es"), id="caso_norm_mayus"),
    ]
)

def test_normaliz_email_casos_validos(email, esperado):
    assert normalizar_email(email) == esperado

def test_caso_invalido_sin_arroba():
    with pytest.raises(ValueError):
        normalizar_email("miemailyaju.com")

def test_caso_invalido_doble_arroba():
    with pytest.raises(ValueError):
        normalizar_email("miemail@@yaju.com")