def find_subsets(nums):
    subsets = [[]]
    for num in nums:
        subsets += [subset + [num] for subset in subsets]
    return subsets


# Ejemplo de uso
numbers = [1, 2, 3]

result = find_subsets(numbers)

print("Subconjuntos sin duplicados:")
for subset in result:
    print(subset)
