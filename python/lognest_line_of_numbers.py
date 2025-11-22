def find_longest_sequence(arr: list[int]) -> list[int]:
    final_arr: list[int] = [arr[0]]
    last_arr: list[int] = []

    last_n: int = arr[0]

    for n in arr:
        if n > last_n:
            final_arr.append(n)
        else:
            if len(final_arr) > len(last_arr):
                last_arr = final_arr
            final_arr = [n]
        last_n = n

    return final_arr if len(final_arr) > len(last_arr) else last_arr


if __name__ == "__main__":
    result: list[int] = find_longest_sequence([1, 2, 3, 1, 2, 3, 3, 4, 5, 6, 7])
    print(result)
