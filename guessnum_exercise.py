def find_first_repeating_character(s):
    # Dictionary to store the count of each character encountered
    char_count = {}

    # Iterate through the characters in the string
    for char in s:
        if char in char_count:
            # If character is already in the dictionary, it's the first repeating character
            print(f"First repeating character: '{char}', Memory address: {id(char)}")
            return char
        else:
            # Add character to the dictionary with a count of 1
            char_count[char] = 1
    
    # If no repeating character is found, return None
    return None

# Test cases
print(find_first_repeating_character("hello"))  # Output should be 'l' and its memory address
print(find_first_repeating_character("python"))  # Output should be None
print(find_first_repeating_character("swiss"))  # Output should be 's' and its memory address
print(find_first_repeating_character("abba"))   # Output should be 'b' and its memory address
