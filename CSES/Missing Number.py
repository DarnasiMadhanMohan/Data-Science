def find_missing_number(n, numbers):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the provided numbers
    actual_sum = sum(numbers)
    
    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum

# Example usage
if __name__ == "__main__":
    # Read the input
    n = int(input("Enter the value of n: "))
    numbers = list(map(int, input(f"Enter {n-1} numbers: ").split()))

    # Find and print the missing number
    missing_number = find_missing_number(n, numbers)
    print("The missing number is:", missing_number)
