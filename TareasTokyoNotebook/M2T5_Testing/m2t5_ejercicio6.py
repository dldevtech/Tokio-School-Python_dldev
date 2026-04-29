def normalizar_email(email: str):
    if email.count('@') != 1:
        raise ValueError('email inválido')
    usuario, dominio = email.split('@')
    return usuario.lower(), dominio.lower()