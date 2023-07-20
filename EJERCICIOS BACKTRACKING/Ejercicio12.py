from itertools import combinations

def find_subsets_of_size(nums, k):
    subsets = list(combinations(nums, k))
    return subsets


# Ejemplo de uso
numbers = [1, 2, 3, 4, 5]
k = 3

result = find_subsets_of_size(numbers, k)

print(f"Subconjuntos de tamaño {k}:")
for subset in result:
    print(subset)
