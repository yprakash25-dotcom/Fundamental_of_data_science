def unique_sorted_list(numbers: list[int]) -> list[int]:
    return sorted(set(numbers))


if __name__ == "__main__":
    raw_numbers = input("Enter numbers separated by spaces: ").strip().split()
    try:
        number_list = [int(item) for item in raw_numbers]
        print(f"Unique sorted result: {unique_sorted_list(number_list)}")
    except ValueError:
        print("Invalid number entered.")
