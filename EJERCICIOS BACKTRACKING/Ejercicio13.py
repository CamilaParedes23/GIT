from itertools import combinations_with_replacement

def find_combinations_with_repetitions(nums, k):
    combinations = list(combinations_with_replacement(nums, k))
    return combinations


# Ejemplo de uso
numbers = [1, 2, 3]
k = 2

result = find_combinations_with_repetitions(numbers, k)

print(f"Combinaciones de {k} elementos permitiendo repeticiones:")
for combination in result:
    print(combination)
