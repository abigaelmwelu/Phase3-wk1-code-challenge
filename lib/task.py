def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2

# Test cases
print(exactly_two_positive(1, 2, -3))  # Output: True
print(exactly_two_positive(-1, 0, 3))  # Output: True
print(exactly_two_positive(0, -2, -3)) # Output: False
