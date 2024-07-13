def collatz_sequence(n, memo={}):
    original_n = n
    sequence = []
    
    while n != 1:
        if n in memo:
            sequence.extend(memo[n])
            break
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    sequence.append(1)
    memo[original_n] = sequence

    print(" ".join(map(str, sequence)))

# Example usage:
n = int(input())  # Read input
collatz_sequence(n)  # Generate and print the sequence