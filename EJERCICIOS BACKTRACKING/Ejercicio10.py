def find_subsets_with_multiple(nums, target):
    subsets = []
    current_subset = []
    backtrack(nums, target, 0, 1, current_subset, subsets)
    return subsets


def backtrack(nums, target, start, current_product, current_subset, subsets):
    if current_product % target == 0:
        subsets.append(current_subset[:])

    for i in range(start, len(nums)):
        num = nums[i]
        if num == 0 or current_product % num == 0:
            current_subset.append(num)
            backtrack(nums, target, i + 1, current_product * num, current_subset, subsets)
            current_subset.pop()


# Ejemplo de uso
numbers = [1, 2, 3, 4, 5]
target = 6

result = find_subsets_with_multiple(numbers, target)

print("Subconjuntos con producto múltiplo de", target)
for subset in result:
    print(subset)
