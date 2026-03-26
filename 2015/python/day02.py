
def part1(input: list[str]) -> int:
    """
    l - length
    w - width
    h - height
    
    Perfect rectangular prism
        - SA = 2*l*w + 2*w*h + 2*h*l
    """
    total_wrapping_paper = 0
    
    for line in input:
        m = sorted(list(map(lambda x: int(x), line.split("x"))))
        l, w, h = m
    
        surface_area = (2 * l * w) + (2 * w * h) + (2 * h * l)
        slack = (l * w)
        
        total_wrapping_paper += surface_area + slack
    return total_wrapping_paper

def part2(input: list[str]) -> int:
    total_ribbon = 0
    for line in input:
        l, w, h = sorted(map(int, line.split("x")))
        
        wrap = 2 * l + 2 * w  # smallest perimeter 
        bow = l * w * h        # volume
        
        total_ribbon += wrap + bow
    
    return total_ribbon


with open("input.txt", "r") as f:
    f = f.readlines()
    print(part1(f))
    print(part2(f))
        



