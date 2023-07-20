def find_permutations(nums):
    permutations = []
    backtrack(nums, [], permutations)
    return permutations


def backtrack(nums, current_permutation, permutations):
    if len(nums) == 0:
        permutations.append(current_permutation[:])
        return

    for i in range(len(nums)):
        num = nums[i]
        remaining_nums = nums[:i] + nums[i+1:]
        current_permutation.append(num)
        backtrack(remaining_nums, current_permutation, permutations)
        current_permutation.pop()


# Ejemplo de uso
numbers = [1, 2, 3]

result = find_permutations(numbers)

print("Permutaciones:")
for permutation in result:
    print(permutation)

