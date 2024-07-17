#You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
#The only input line contains a string of n characters.
#Output
#Print one integer: the length of the longest repetition.
#Constraints

#1 \le n \le 10^6

#Example
#Input:
#ATTCGGGA

def longest_repetition(s):
    max_len = 1
    current_len = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1
    
    # Final check at the end of the string
    if current_len > max_len:
        max_len = current_len
    
    return max_len

# Read the input string
s = input()

# Find and print the length of the longest repetition
print(longest_repetition(s))


#Output:
#3