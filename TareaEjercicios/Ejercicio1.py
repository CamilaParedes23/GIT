#verificar su una lista está ordenada de
#forma ascendete
def esta_ordenada_ascendente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True

# Ejemplo del programa
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [1, 3, 2, 4, 5]

if esta_ordenada_ascendente(lista_1):
    print("La lista 1 está ordenada de forma ascendente.")
else:
    print("La lista 1 no está ordenada de forma ascendente.")

if esta_ordenada_ascendente(lista_2):
    print("La lista 2 está ordenada de forma ascendente.")
else:
    print("La lista 2 no está ordenada de forma ascendente.")
