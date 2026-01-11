from typing import List


def firstMissingPosition(nums: List[int]) -> int:
    sorted_nums = sorted(set(nums))
    last_number = 0
    for n in sorted_nums:
        if n <= 0:
            continue

        if n > last_number and n == last_number + 1:
            last_number = n
            continue
        else:
            break

    return last_number + 1


def firstMissingPosition2(nums: List[int]) -> int:
    nums_set = sorted(set(nums))

    i = 1
    while i in nums_set:
        i += 1

    return i


def main():
    nums: List[int] = [1, 2, 0]
    nums2: List[int] = [3, 4, -1, 1]
    nums3: List[int] = [7, 8, 9, 11, 12]
    nums4: List[int] = [100000, 3, 4000, 2, 15, 1, 99999]
    missing_num: int = firstMissingPosition(nums4)
    missing_num2: int = firstMissingPosition2(nums2)

    print(missing_num)
    print(missing_num2)


if __name__ == "__main__":
    main()
