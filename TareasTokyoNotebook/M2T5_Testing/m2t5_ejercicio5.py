def filtrar_aprobados(pares):
    resultado = []
    for nombre, nota in pares:
        if nota >= 5:
            resultado.append(nombre)
    return resultado

resultado = filtrar_aprobados(([("Diego", 6), ("Cesaria", 8), ("Logan", 7)]))
print(resultado)