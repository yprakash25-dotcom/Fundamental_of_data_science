
positive_sum = 0  # Accumulate sum of non-negative numbers
negative_sum = 0  # Accumulate sum of negative numbers

while True:  # Keep showing the menu until the user exits
    print("\n1. Enter Number")  # Menu option to enter a number
    print("2. Exit")  # Menu option to exit the loop

    choice = input("Choose option: ")  # Read the menu choice

    if choice == '1':  # Handle number entry option
        num = float(input("Enter number: "))  # Read a number from the user
        if num >= 0:  # Check if the number is non-negative
            positive_sum += num  # Add to positive sum
        else:
            negative_sum += num  # Add to negative sum
    elif choice == '2':  # Handle exit option
        break  # Exit the loop
    else:
        print("Invalid choice")  # Handle invalid menu choice

print("\nSum of positive numbers:", positive_sum)  # Display sum of positives
print("Sum of negative numbers:", negative_sum)  # Display sum of negatives
