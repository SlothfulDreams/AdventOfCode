from collections import Counter
from typing import List

# Part One
left_column: list = []
right_column: list = []


def read_columns(file_path: str) -> tuple[List[int], List[int]]:
    left_column, right_column = [], []

    try:
        with open(file_path, "r") as f:
            for content in f:
                columns = content.split()
                left_column.append(int(columns[0]))
                right_column.append(int(columns[1]))
    except Exception as error:
        print(error)

    left_column.sort()
    right_column.sort()

    return left_column, right_column


def calc_distance(left: List[int], right: List[int]) -> int:
    return sum(map(lambda x, y: abs(y - x), left_column, right_column))


left_column, right_column = read_columns("input.txt")

print(calc_distance(left_column, right_column))


# Part Two

def calc_similarity_score(column: List[int]) -> int:
    similarity_score = 0
    count_right_column = Counter(right_column)
    for val in column:
        if val in count_right_column.keys():
            similarity_score += count_right_column[val] * val
    return similarity_score


print(calc_similarity_score(left_column))
