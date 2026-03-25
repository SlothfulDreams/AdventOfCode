"""
( - Move up
) - Move down

Find the floor Santa is on
"""

def part1(input: str) -> int:
    floor = 0
    for char in input:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    return floor
    
        
def part2(input: str) -> int | None:
    floor = 0
    for index, char in enumerate(input):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        
        if floor == -1:
            return index + 1
    return None

with open("input.txt", "r") as f:
    f = f.read()
    print(part1(f))
    print(part2(f))
    