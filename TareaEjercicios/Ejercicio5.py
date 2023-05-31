#Verificar si una lista es simétrica
def es_simetrica(lista):
    longitud = len(lista)
    for i in range(longitud // 2):
        if lista[i] != lista[longitud - i - 1]:
            return False
    return True

# Ejemplo del programa
lista_1 = [1, 2, 3, 3, 2, 1]
lista_2 = [1, 2, 3, 4, 5, 6]

if es_simetrica(lista_1):
    print("La lista 1 es simétrica.")
else:
    print("La lista 1 no es simétrica.")

if es_simetrica(lista_2):
    print("La lista 2 es simétrica.")
else:
    print("La lista 2 no es simétrica.")
