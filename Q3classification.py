
num = int(input("Enter a number: "))  # Read an integer to classify

if num > 0:  # Check if the number is positive
    if num % 2 == 0:  # Check if the positive number is even
        print("Positive Even")  # Output classification
    else:
        print("Positive Odd")  # Output classification
elif num < 0:  # Check if the number is negative
    if num % 2 == 0:  # Check if the negative number is even
        print("Negative Even")  # Output classification
    else:
        print("Negative Odd")  # Output classification
else:
    print("Zero")  # Handle the zero case
