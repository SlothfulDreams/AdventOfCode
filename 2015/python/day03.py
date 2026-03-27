def part1(input: str) -> int:
    """
    Origin - Starting location
    ^ - north
    v - southprint(part2(["^", "v", "^", "v", "^", "v", "^", "v", "^", "v"]))
    > - east
    < - west
    
    Each directon counts as a house, including origin
    But we can always move back to the same house
    
    Find the number of unique houses visited
    
    Ex)
    > - 2 houses counting origin
    ^v^v - 2 houses, one house a the origin and one house north
    """
    house_posn = {(0, 0)}
    
    total_houses = 1
    
    north_south = 0
    east_west = 0
    
    for direction in input:
        match direction:
            case "^":
                north_south += 1
            case "v":
                north_south -= 1
                
            case "<":
                east_west -= 1
            case ">":
                east_west += 1
        coords = (north_south, east_west)
        
        if coords not in house_posn:
            total_houses += 1
            house_posn.add(coords)
        
    return total_houses

def part2(input: str) -> int:
    """
    Santa and robo santa alternate position
    """
    global_house_posn: set[tuple[int, int]] = {(0, 0)}
    positions = {"santa": [0, 0], "robo": [0, 0]}
    isSantaTurn = True

    for direction in input:
        pos = positions["santa"] if isSantaTurn else positions["robo"]

        match direction:
            case "^": pos[0] += 1
            case "v": pos[0] -= 1
            case "<": pos[1] -= 1
            case ">": pos[1] += 1

        coords = (pos[0], pos[1])
        if coords not in global_house_posn:
            global_house_posn.add(coords)

        isSantaTurn = not isSantaTurn

    return len(global_house_posn)  
            

with open("input.txt", "r") as f:
    lines = f.readline()
    print(part1(lines))
    print(part2(lines))