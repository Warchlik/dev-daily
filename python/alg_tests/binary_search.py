def main(arr: list[int], len: int, search: int):

    left: int = 0
    right: int = len - 1

    while left <= right:
        m: int = (left + right) // 2
        if arr[m] == search:
            return m
        else:
            if arr[m] > search:
                right = m - 1
            else:
                left = m + 1

    return -1


if __name__ == "__main__":
    arr: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
    index: int = main(arr, len(arr), 9)
    print(index)
