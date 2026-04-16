def reverse_sort_names(names: list[str]) -> list[str]:
    return sorted(names, reverse=True)


if __name__ == "__main__":
    print("Question 5: Reverse alphabetical student list")
    names_input = input("Enter student names separated by commas: ").strip()
    names = [name.strip() for name in names_input.split(",") if name.strip()]
    if names:
        sorted_names = reverse_sort_names(names)
        print(f"Original names: {names}")
        print(f"Reverse sorted: {sorted_names}")
    else:
        print("No valid student names provided.")
