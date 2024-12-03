import re


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


def parse_program(program):
    pattern = r"mul\((\d+),(\d+)\)"
    return re.findall(pattern, program)


def parse_program_p2(program):
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    return re.finditer(pattern, program)


def calc_all_mul(matches):
    total_sum = 0
    for match in matches:
        x, y = int(match[0]), int(match[1])
        total_sum += x * y
    return total_sum


def calc_all_mul_p2(matches):
    mul_enabled = True
    total_sum = 0
    for match in matches:
        if match.group(0) == "do()":
            mul_enabled = True
        elif match.group(0) == "don't()":
            mul_enabled = False
        elif match.group(1) and match.group(2):
            if mul_enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total_sum += x * y
    return total_sum


def process_file(file_path, part):
    program = read_file(file_path)
    if part == 1:
        matches = parse_program(program)
        return calc_all_mul(matches)
    elif part == 2:
        matches = parse_program_p2(program)
        return calc_all_mul_p2(matches)


def main():
    files = {
        "Part 1": {
            "example": "../data/day3-example.txt",
            "test": "../data/day3-test.txt",
        },
        "Part 2": {
            "example": "../data/day3-example-p2.txt",
            "test": "../data/day3-test.txt",
        },
    }
    for part, paths in files.items():
        print(f"[{part}]")
        for case, file_path in paths.items():
            result = process_file(file_path, int(part.split()[-1]))
            print(f"{case.capitalize()}: {result}")
        print()


if __name__ == "__main__":
    main()
