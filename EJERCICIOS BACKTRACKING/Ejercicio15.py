def find_combinations(nums, target):
    combinations = []
    backtrack(nums, target, 0, [], combinations)
    return combinations


def backtrack(nums, target, start, current_combination, combinations):
    current_sum = sum(current_combination)

    if current_sum == target:
        combinations.append(current_combination[:])
        return

    if current_sum > target:
        return

    for i in range(start, len(nums)):
        current_combination.append(nums[i])
        backtrack(nums, target, i, current_combination, combinations)
        current_combination.pop()


# Ejemplo de uso
numbers = [2, 4, 6, 8, 10]
target_sum = 16

result = find_combinations(numbers, target_sum)

print("Combinaciones con suma igual a", target_sum)
for combination in result:
    print(combination)
