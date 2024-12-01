from collections import Counter

# Part One
left_column: list = []
right_column: list = []


with open("input.txt", "r") as f:
    for content in f:
        columns = content.split()
        left_column.append(int(columns[0]))
        right_column.append(int(columns[1]))

left_column = sorted(left_column)
right_column = sorted(right_column)

distances = list(map(lambda x, y: abs(y - x), left_column, right_column))

print(sum(distances))

# Part Two

similarity_score = 0

count_right_column = Counter(right_column)

for val in left_column:
    if val in count_right_column.keys():
        similarity_score += count_right_column[val] * val

print(similarity_score)
