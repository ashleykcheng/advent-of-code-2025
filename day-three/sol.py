import sys

def part_one(filename):
    def helper(input):
        ordering = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
        for num in ordering:
            if num in input:
                return (num, input.index(num))

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    result = 0
    
    for line in lines:
        first_num, first_pos = helper(line[:-1])
        second_num, second_pos = helper(line[first_pos + 1:])
        result += int(first_num + second_num)
    
    return result 

def part_two(filename):
    def helper(input):
        ordering = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
        for num in ordering:
            if num in input:
                return (num, input.index(num))
    
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    result = 0
    
    for line in lines:
        n = len(line)
        if n < 12:
            continue
        
        selected = []
        start = 0
        remaining = 12
        
        while remaining > 0 and start < n:
            # We need to leave (remaining - 1) digits after the current selection
            # So we can only look from start to n - (remaining - 1)
            end = n - remaining + 1
            search_range = line[start:end]
            
            # Use helper to find the largest digit in the available range
            max_digit, relative_pos = helper(search_range)
            max_pos = start + relative_pos
            
            selected.append(max_digit)
            start = max_pos + 1
            remaining -= 1
        
        result += int(''.join(selected))
    
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    print("Part 1:", part_one(filename))
    print("Part 2:", part_two(filename))
