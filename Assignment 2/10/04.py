str1 = "PyNaTive"
lower_chars = ""
upper_chars = ""
for char in str1:
    if char.islower():
        lower_chars += char
    else:
        upper_chars += char
sorted_string = lower_chars + upper_chars
print(sorted_string)