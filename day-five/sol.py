import sys

def part_one(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Parse ranges (until empty line)
    ranges = []
    numbers = []
    empty_line_found = False
    
    for line in lines:
        line = line.strip()
        if not line:
            empty_line_found = True
            continue
        
        if not empty_line_found:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
        else:
            numbers.append(int(line))
    
    # Merge overlapping intervals
    if ranges:
        ranges.sort(key=lambda x: x[0])
        merged = [ranges[0]]
        for current_start, current_end in ranges[1:]:
            last_start, last_end = merged[-1]
            if current_start <= last_end:
                merged[-1] = (last_start, max(last_end, current_end))
            else:
                merged.append((current_start, current_end))
        ranges = merged

    numbers = sorted(numbers)

    # Count how many numbers fall into at least one range
    # Two-pointer approach: O(n + m) since both lists are sorted
    curr_range_idx = 0
    fresh_count = 0
    for num in numbers:
        # Advance to the first range that could contain num (or past all ranges)
        while curr_range_idx < len(ranges) and ranges[curr_range_idx][1] < num:
            curr_range_idx += 1
        
        # Check if num falls into the current range
        if curr_range_idx < len(ranges):
            start, end = ranges[curr_range_idx]
            if start <= num <= end:
                fresh_count += 1
    
    print(f"Ranges: {ranges}")
    print(f"Numbers: {numbers}")
    print(f"Fresh ingredient IDs: {fresh_count}")
    return fresh_count

def part_two(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Parse ranges (until empty line)
    ranges = []
    numbers = []
    empty_line_found = False
    
    for line in lines:
        line = line.strip()
        if not line:
            break
        
        if not empty_line_found:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
    
    # Merge overlapping intervals
    if ranges:
        ranges.sort(key=lambda x: x[0])
        merged = [ranges[0]]
        for current_start, current_end in ranges[1:]:
            last_start, last_end = merged[-1]
            if current_start <= last_end:
                merged[-1] = (last_start, max(last_end, current_end))
            else:
                merged.append((current_start, current_end))
        ranges = merged

    count = 0
    for start, end in ranges:
        count += end - start + 1

    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    print(part_two(filename))
