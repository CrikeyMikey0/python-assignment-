def is_balanced(s1, s2):
    for char in s1:
        if char not in s2:
            return False
    return True

# Case 1
s1 = "Yn"
s2 = "PYnative"
print(is_balanced(s1, s2))

# Case 2
s1 = "Ynf"
s2 = "PYnative"
print(is_balanced(s1, s2))