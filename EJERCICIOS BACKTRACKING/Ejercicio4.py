#UNIVERSIDAD DE LAS FUERZAS ARMADAS "ESPE"
#NOMBRE: PAREDES PANATA CAMILA SOLEDAD
#NRC: 9898
#FECHA: 19/07/2023
def find_subsets_with_sum(nums, target):
    subsets = []
    current_subset = []
    backtrack(nums, target, 0, current_subset, subsets)
    return subsets


def backtrack(nums, target, start, current_subset, subsets):
    if sum(current_subset) == target:
        subsets.append(current_subset[:])

    if sum(current_subset) > target:
        return

    for i in range(start, len(nums)):
        current_subset.append(nums[i])
        backtrack(nums, target, i + 1, current_subset, subsets)
        current_subset.pop()


# Ejemplo de uso
numbers = [2, 4, 6, 8, 10]
target_sum = 16

result = find_subsets_with_sum(numbers, target_sum)

print("Subconjuntos con suma igual a", target_sum)
for subset in result:
    print(subset)
