from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for m in matrix:
        if target in m:
            return True

    return False


def main():
    # https://leetcode.com/problems/search-a-2d-matrix/description/?envType=problem-list-v2&envId=arrays
    matrix: List[List[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target: int = 3
    output: bool = searchMatrix(matrix=matrix, target=target)
    print(output)


if __name__ == "__main__":
    main()
