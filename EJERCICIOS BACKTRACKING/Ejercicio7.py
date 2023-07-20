def find_subsets_within_range(nums, target_range):
    subsets = []
    current_subset = []
    backtrack(nums, target_range, 0, current_subset, subsets)
    return subsets


def backtrack(nums, target_range, start, current_subset, subsets):
    current_sum = sum(current_subset)

    if target_range[0] <= current_sum <= target_range[1]:
        subsets.append(current_subset[:])

    if current_sum > target_range[1]:
        return

    for i in range(start, len(nums)):
        current_subset.append(nums[i])
        backtrack(nums, target_range, i + 1, current_subset, subsets)
        current_subset.pop()


# Ejemplo de uso
numbers = [2, 4, 6, 8, 10]
target_range = (10, 20)

result = find_subsets_within_range(numbers, target_range)

print("Subconjuntos con suma dentro del rango", target_range)
for subset in result:
    print(subset)
