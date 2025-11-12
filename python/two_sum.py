# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


def two_sum(int_list: list[int], sum: int) -> list[int]:
    last_number: int = 0
    last_index: int = 0

    result_arr: list[int] = []
    for i, n in enumerate(int_list):
        if not i > 0:
            last_index = i
            last_number = n
            continue

        if last_number + n == sum:
            result_arr.append(last_index)
            result_arr.append(i)
            break

        last_index = i
        last_number = n

    return result_arr


if __name__ == "__main__":
    array: list[int] = [1, 2, 3, 2, 8, 4, 9, 0, 4, 5]
    number: int = 3
    result = two_sum(array, number)
    print(result)
