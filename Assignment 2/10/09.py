str1 = "PYnative29@#8496"
total_sum, count = 0, 0
for char in str1:
    if char.isdigit():
        total_sum += int(char)
        count += 1
average = total_sum / count
print(f"Sum is: {total_sum} Average is {average}")