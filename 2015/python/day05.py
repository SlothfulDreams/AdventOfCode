def part1(input: str) -> bool:
    """
    Nice String one of the following props
    - contains >= three vowels (aeiou)
    - one letter that appeears twice in a row
    - DOES NOT contain 'ab', 'cd', 'pq' or 'xy'
    """
    vowel_set = set("aeiou")
    cannot_contain = {"ab", "cd", "pq", "xy"}

    vowels = 0

    for s in cannot_contain:
        if s in input:
            return False

    for c in input:
        if c in vowel_set:
            vowels += 1

    appear_twice = False
    for i in range(1, len(input)):
        if input[i - 1] == input[i]:
            appear_twice = True

    return appear_twice and vowels >= 3

def part2(input: str) -> bool:
    # Rule 1: any pair appears twice without overlapping
    rule1 = any(input[i:i+2] in input[i+2:] for i in range(len(input) - 1))
    
    # Rule 2: any letter repeats with exactly one between them
    rule2 = any(input[i] == input[i+2] for i in range(len(input) - 2))
    
    return rule1 and rule2




with open("input.txt", "r") as file:
    f = file.readlines()
    total_nice = 0
    total_nice_p2 = 0

    for string in f:
        if part1(string):
            total_nice += 1
        
        if part2(string):
            total_nice_p2 += 1
    print(total_nice)
    print(total_nice_p2)
    
    