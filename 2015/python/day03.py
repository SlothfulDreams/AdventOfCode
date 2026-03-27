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
    robot verison of santa, alternate turns with actual santa
    """
    global_house_posn = {(0, 0)}
    
    total_houses = 1
    
    robo_north_south = 0
    robo_east_west = 0
    
    santa_north_south = 0
    santa_east_west = 0
    
    isSantaTurn = True
    
    for direction in input:
        if isSantaTurn:
            match direction:
                case "^":
                    santa_north_south += 1
                case "v":
                    santa_north_south -= 1
                    
                case "<":
                    santa_east_west -= 1
                case ">":
                    santa_east_west += 1
            
            coords = (santa_north_south, santa_east_west)
            
            if coords not in global_house_posn:
                total_houses += 1
                global_house_posn.add(coords)
        else:
            match direction:
                case "^":
                    robo_north_south += 1
                case "v":
                    robo_north_south -= 1
                    
                case "<":
                    robo_east_west -= 1
                case ">":
                    robo_east_west += 1
            
            coords = (robo_north_south, robo_east_west)
            
            if coords not in global_house_posn:
                total_houses += 1
                global_house_posn.add(coords)
        isSantaTurn = not isSantaTurn
                
    return total_houses
            
print(part2("^v^v^v^v^v"))


with open("input.txt", "r") as f:
    lines = f.readline()
    print(part1(lines)) # 2081
    print(part2(lines)) # 2341