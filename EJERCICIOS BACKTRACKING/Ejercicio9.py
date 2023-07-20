from itertools import combinations

def find_combinations(nums, k):
    combinations_list = list(combinations(nums, k))
    return combinations_list


# Ejemplo de uso
numbers = [1, 2, 3, 4, 5]
k = 3

result = find_combinations(numbers, k)

print(f"Combinaciones de {k} elementos:")
for combination in result:
    print(combination)
