filename = "pi_digits.txt"

with open(filename, 'w') as f:
    f.write("hahahahhha")
with open(filename) as b:
    contents = b.readline()
print(contents)
