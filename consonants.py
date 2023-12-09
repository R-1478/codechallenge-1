def solve(s):
    vowels = "aeiou"
    
    # Function to calculate the value of a substring
    def substring_value(sub):
        return sum(ord(char) - ord('a') + 1 for char in sub)

    # Initialize variables to store maximum value
    max_value = 0
    current_value = 0

    # Iterate through the string
    for char in s:
        if char in vowels:
            # Reset current value if a vowel is encountered
            current_value = 0
        else:
            # Update current value for consonants
            current_value += ord(char) - ord('a') + 1
            # Update maximum value if current value is higher
            max_value = max(max_value, current_value)

    return max_value

# Examples
print(solve("zodiacs"))  # Output: 26
print(solve("strength"))  # Output: 57
