def part_one():
    with open("input.txt", "r") as file:
        """
        L Dial- Decrease
        R Dial - Increase

        Start Dial - 50

        Circle - (0 - 99)
        """
        content = file.read()
        start = 50
        ans = 0

        for line in content.splitlines():
            dial = list(line)
            direction = dial[0]

            magnitude = int("".join(dial[1::]))

            if direction == "L":
                start = (start - magnitude) % 100

            elif direction == "R":
                start = (start + magnitude) % 100

            if start == 0:
                ans += 1
    return ans


# print(part_one())
