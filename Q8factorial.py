# Q8_factorial.py  # File label for factorial calculation

num = input("Enter a number: ")  # Read input as a string

if num.isdigit():  # Validate that the input is a positive integer
    num = int(num)  # Convert input to integer
    fact = 1  # Initialize factorial accumulator
    for i in range(1, num + 1):  # Multiply from 1 to num
        fact *= i  # Update factorial result
    print("Factorial:", fact)  # Display factorial
else:
    print("Invalid input! Please enter a positive integer.")  # Handle invalid input
