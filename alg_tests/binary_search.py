def main(arr: list[int], len: int, search: int):

    l: int = 0
    r: int = len - 1

    while l <= r:
        m: int = (l + r) // 2
        if arr[m] == search:
            return m
        else:
            if arr[m] > search:
                r = m - 1
            else:
                l = m + 1

    return -1


if __name__ == "__main__":
    arr: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
    index: int = main(arr, len(arr), 9)
    print(index)
