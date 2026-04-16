def arithmetic_operations(a: int, b: int) -> None:
    print("\nQuestion 1: Arithmetic operations")
    print(f"Inputs: a = {a}, b = {b}")
    print(f"Sum       : {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product   : {a * b}")
    if b != 0:
        print(f"Quotient  : {a / b:.2f}")
    else:
        print("Quotient  : Division by zero is not allowed")


if __name__ == "__main__":
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        arithmetic_operations(a, b)
    except ValueError:
        print("Invalid integer input.")
