str1 = "P@#yn26at^&i5ve"
char_count, digit_count, symbol_count = 0, 0, 0
for char in str1:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1
print("Total counts of chars, digits, and symbols")
print(f"\nChars = {char_count}\nDigits = {digit_count}\nSymbol = {symbol_count}")