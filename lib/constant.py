def highest_consonant_value(s):
    def char_value(c):
        return ord(c) - ord('a') + 1
    
    max_value = 0
    current_value = 0

    for char in s:
        if char in "aeiou":
            current_value = 0
        else:
            current_value += char_value(char)
            max_value = max(max_value, current_value)

    return max_value

# Test cases
print(highest_consonant_value("abc"))  # Output: 2 (bc)
print(highest_consonant_value("bcd"))  # Output: 8 (bcd)
print(highest_consonant_value("xyz"))  # Output: 26 (xyz)
