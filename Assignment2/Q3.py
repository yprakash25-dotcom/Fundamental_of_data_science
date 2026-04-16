def is_armstrong_string(value: str) -> bool:
    if not value.isdigit():
        raise ValueError("Input must contain only digits.")
    number = int(value)
    digits = [int(d) for d in value]
    power = len(digits)
    return number == sum(d ** power for d in digits)


if __name__ == "__main__":
    number_string = input("Enter a number string to check Armstrong: ").strip()
    try:
        if is_armstrong_string(number_string):
            print(f"{number_string} is an Armstrong number.")
        else:
            print(f"{number_string} is not an Armstrong number.")
    except ValueError as exc:
        print(exc)
