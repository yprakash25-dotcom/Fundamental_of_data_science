def add(x: float, y: float) -> float:
    return x + y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> str:
    return f"{x / y:.2f}" if y != 0 else "Undefined (division by zero)"


def floor_divide(x: float, y: float) -> str:
    return f"{x // y:.0f}" if y != 0 else "Undefined (division by zero)"


def exponentiate(x: float, y: float) -> float:
    return x ** y


if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("\nQuestion 2: Separate operations")
        print(f"Addition       : {add(a, b)}")
        print(f"Multiplication : {multiply(a, b)}")
        print(f"Division       : {divide(a, b)}")
        print(f"Floor Division : {floor_divide(a, b)}")
        print(f"Exponentiation : {exponentiate(a, b)}")
    except ValueError:
        print("Invalid number input.")
