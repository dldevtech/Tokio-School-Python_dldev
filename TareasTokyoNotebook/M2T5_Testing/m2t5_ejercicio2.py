def es_palindromo(s: str) -> bool:
    s = s.lower().replace(' ', '')
    return s == s[::-1]