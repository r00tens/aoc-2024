def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            left_list = []
            right_list = []
            for line in lines:
                left, right = map(int, line.strip().split())
                left_list.append(left)
                right_list.append(right)
            return left_list, right_list
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)


def calc_total_distance(left_list, right_list):
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)
    total_distance = sum(abs(left - right) for left, right in zip(left_list_sorted, right_list_sorted))
    return total_distance


def calc_similarity_score(left_list, right_list):
    similarity_score = sum(left * right_list.count(left) for left in left_list)
    return similarity_score


def process_file(file_path):
    left_list, right_list = read_file(file_path)
    total_distance = calc_total_distance(left_list, right_list)
    similarity_score = calc_similarity_score(left_list, right_list)
    print(f"Total distance: {total_distance}")
    print(f"Similarity score: {similarity_score}")


def main():
    example_file_path = "../data/day1-example.txt"
    test_file_path = "../data/day1-test.txt"
    print("Example:")
    process_file(example_file_path)
    print("\nInput:")
    process_file(test_file_path)


if __name__ == "__main__":
    main()
