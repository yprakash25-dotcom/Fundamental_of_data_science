# Q6_primes.py  # File label for prime number operations

start = int(input("Enter start: "))  # Read the starting value
end = int(input("Enter end: "))  # Read the ending value

primes = []  # Store prime numbers found in the range

for num in range(start, end + 1):  # Check each number in the range
    if num > 1:  # Primes are greater than 1
        for i in range(2, int(num**0.5) + 1):  # Try factors up to sqrt(num)
            if num % i == 0:  # If divisible, it's not prime
                break  # Exit the factor loop
        else:
            primes.append(num)  # Add prime numbers to the list

print("Prime numbers:", primes)  # Display all primes found
print("Count:", len(primes))  # Display count of primes
print("Sum:", sum(primes))  # Display sum of primes
