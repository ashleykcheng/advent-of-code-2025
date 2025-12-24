import sys

def part_one(filename):
    with open(filename, 'r') as f:
        input = f.readline()
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    part_one(filename)
