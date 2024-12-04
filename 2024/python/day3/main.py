import re

with open('input.txt', 'r') as f:
    f_content = f.read()


def regex_extraction(memory):
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    # Find all matches for mul(X,Y)
    matches = re.findall(pattern, memory)

    total = 0
    for x, y in matches:
        total += int(x) * int(y)

    return total


print(regex_extraction(f_content))


# Part 2


def solve_corrupted_memory(memory_string):

    mul_enabled = True

    results = []

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'

    for match in re.finditer(pattern, memory_string):
        if match.group() == 'do()':

            mul_enabled = True
        elif match.group() == 'don\'t()':

            mul_enabled = False
        elif mul_enabled:

            a, b = map(int, match.groups())
            results.append(a * b)

    return sum(results)


print(solve_corrupted_memory(f_content))
