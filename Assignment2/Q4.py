def count_occurrences(numbers: list[int]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts


if __name__ == "__main__":
    test_lists = [
        [1, 2, 2, 3, 3, 3],
        [5, 5, 5, 5],
        [10, 20, 10, 30, 20, 10],
    ]
    print("Question 4: Number occurrence counts")
    for idx, test_list in enumerate(test_lists, 1):
        print(f"\nTest list {idx}: {test_list}")
        print(f"Counts: {count_occurrences(test_list)}")
