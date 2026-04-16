"""Generate a NumPy array and compute sum, mean, max, and min values."""

import numpy as np


def main() -> None:
    numbers = np.array([10, 20, 30, 40, 50])
    print("Question 1: NumPy array operations")
    print("Array:", numbers)
    print("Total sum:", np.sum(numbers))
    print("Mean value:", np.mean(numbers))
    print("Largest value:", np.max(numbers))
    print("Smallest value:", np.min(numbers))


if __name__ == "__main__":
    main()
