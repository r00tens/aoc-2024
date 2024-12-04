def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()


def search_word(data, word):
    rows = len(data)
    cols = len(data[0])
    count_words = 0
    word_length = len(word)
    # dx, dy
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # bottom
        (-1, 0),  # top
        (1, 1),  # bottom right
        (-1, -1),  # top left
        (1, -1),  # bottom left
        (-1, 1),  # top right
    ]
    for dx, dy in directions:
        for i in range(rows):
            for j in range(cols):
                for k in range(word_length):
                    x = i + k * dx
                    y = j + k * dy
                    if x < 0 or x >= rows or y < 0 or y >= cols or data[x][y] != word[k]:
                        break
                else:
                    count_words += 1
    return count_words


def search_word_p2(data):
    rows = len(data)
    cols = len(data[0])
    count_words = 0
    patterns = [
        ['A', 'M', 'S', 'M', 'S'],  # normal X-MAS
        ['A', 'S', 'M', 'S', 'M'],  # horizontally reversed
        ['A', 'M', 'M', 'S', 'S'],  # vertically reversed
        ['A', 'S', 'S', 'M', 'M'],  # fully reversed
    ]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            for pattern in patterns:
                if (
                        data[i][j] == pattern[0] and
                        data[i - 1][j - 1] == pattern[1] and  # top left
                        data[i - 1][j + 1] == pattern[2] and  # top right
                        data[i + 1][j - 1] == pattern[3] and  # bottom left
                        data[i + 1][j + 1] == pattern[4]  # bottom right
                ):
                    count_words += 1
                    break
    return count_words


def main():
    example_file_path = "../data/day4-example.txt"
    test_file_path = "../data/day4-test.txt"
    example_data = read_file(example_file_path)
    test_data = read_file(test_file_path)
    print("[Part 1]")
    print(f"Example: {search_word(example_data, 'XMAS')}")
    print(f"Test: {search_word(test_data, 'XMAS')}")
    print("")
    print("[Part 2]")
    print(f"Example: {search_word_p2(example_data)}")
    print(f"Test: {search_word_p2(test_data)}")


if __name__ == "__main__":
    main()
