import sys

def part_one(input):
    def helper(x, y):
        def is_valid(i, j):
            return 0 <= i < len(input) and 0 <= j < len(input[0])

        num_rolls = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i == x and j == y:
                    continue
                if is_valid(i, j) and input[i][j] == '@':
                    num_rolls += 1
        return num_rolls

    num_accessible = 0
    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] == '@' and helper(row, col) < 4:
                num_accessible += 1
                input[row][col] = 'x'
    return num_accessible
    

def part_two(filename):
    with open(filename, 'r') as f:
        input = [list(line.strip()) for line in f.readlines()]

    total_removed = 0
    while True:
        removed = part_one(input)
        if removed == 0:
            break
        total_removed += removed
    return total_removed



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    print("Part 2:", part_two(filename))
