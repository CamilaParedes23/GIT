#UNIVERSIDAD DE LAS FUERZAS ARMADAS "ESPE"
#NOMBRE: PAREDES PANATA CAMILA SOLEDAD
#NRC: 9898
#FECHA: 19/07/2023
from itertools import product

def find_permutations_with_repetitions(nums, length):
    permutations = list(product(nums, repeat=length))
    return permutations


# Ejemplo de uso
numbers = [1, 2, 3]
length = 3

result = find_permutations_with_repetitions(numbers, length)

print(f"Permutaciones de longitud {length} permitiendo repeticiones:")
for permutation in result:
    print(permutation)
