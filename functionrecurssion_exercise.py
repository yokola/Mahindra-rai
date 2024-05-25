def reverse_string(s):
    # Base case: if the string is empty or has only one character, return it as it is
    if len(s) <= 1:
        return s
    else:
        # Recursive case: reverse the substring from the second character onward
        # and append the first character at the end
        return reverse_string(s[1:]) + s[0]

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("python"))  # Output: "nohtyp"
print(reverse_string(""))        # Output: ""
print(reverse_string("a"))       # Output: "a"
print(reverse_string("ChatGPT")) # Output: "TPGtaC"
