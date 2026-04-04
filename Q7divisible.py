# Q7_divisible.py  # File label for divisibility filter

start = int(input("Enter start: "))  # Read the starting value
end = int(input("Enter end: "))  # Read the ending value

result = []  # Store numbers that meet the divisibility rule

for num in range(start, end + 1):  # Check each number in the range
    if num % 9 == 0 and num % 6 != 0:  # Divisible by 9 but not by 6
        result.append(num)  # Add qualifying numbers to the list

print("Numbers:", result)  # Display the filtered numbers
