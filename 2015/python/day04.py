import hashlib
def part1(input: str) -> int:
    for x in range(99999999999):
        digest = hashlib.md5((input + str(x)).encode()).hexdigest()
        if digest[:5] == "00000":
            return x
    return -1

def part2(input: str) -> int:
    for x in range(99999999999):
        digest = hashlib.md5((input + str(x)).encode()).hexdigest()
        if digest[:6] == "000000":
            return x
    return -1
    


    