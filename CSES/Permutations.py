def beautiful_permutation(n):
    if n == 2 or n == 3:
        return "NO SOLUTION"
    
    even_numbers = [i for i in range(2, n + 1, 2)]
    odd_numbers = [i for i in range(1, n + 1, 2)]
    
    # Combine even and odd lists
    permutation = even_numbers + odd_numbers
    
    # Join numbers into a string for output
    return ' '.join(map(str, permutation))

# Input reading
n = int(input().strip())

# Generate and print the beautiful permutation
print(beautiful_permutation(n))
 