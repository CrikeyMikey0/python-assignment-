s1 = "Abc"
s2 = "Xyz"
s3 = ""
s2_reversed = s2[::-1]
min_len = min(len(s1), len(s2))
for i in range(min_len):
    s3 += s1[i] + s2_reversed[i]
s3 += s1[min_len:] + s2_reversed[min_len:]
print(s3)