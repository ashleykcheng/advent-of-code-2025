import sys

def part_one(filename):
    with open(filename, 'r') as f:
        id_ranges = f.readline()
    id_ranges = id_ranges.split(",")

    invalid = 0

    for id_range in id_ranges:
        parts = id_range.split('-')
        if len(parts) != 2:
            continue

        start, end = parts
        start = int(start)
        end = int(end)

        for i in range(start, end + 1):
            i_str = str(i)
            num_len = len(i_str)
            if num_len % 2 == 1:
                continue

            mid_point = num_len // 2
            if i_str[:mid_point] == i_str[mid_point:]:
                invalid += i

    return invalid

def part_two(filename):
    with open(filename, 'r') as f:
        id_ranges = f.readline()
    id_ranges = id_ranges.split(",")

    invalid = 0

    for id_range in id_ranges:
        parts = id_range.split('-')
        if len(parts) != 2:
            continue

        start, end = parts
        start = int(start)
        end = int(end)

        for i in range(start, end + 1):
            found = set()
            i_str = str(i)
            num_len = len(i_str)

            mid_point = num_len // 2
            for seg_length in range(1, mid_point + 1):
                if num_len % seg_length != 0:
                    continue
                constructed_num = i_str[:seg_length] * (num_len // seg_length)
                if i_str == constructed_num and i not in found:
                    print(i)
                    invalid += i
                    found.add(i)

    print(invalid)
    return invalid

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    part_two(filename)
