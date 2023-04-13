filename = "pi_digits.txt"

with open(filename) as f:
    lines = f.readlines()
pi_string = ''

for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(f"{pi_string[:52]}")
print(len(pi_string))

birthday = input("aaaaaaaaaaa")
if birthday in pi_string:
    print("yyyyyyyyyyyyyyyyy")
else:
    print("nnnnnnnnnn")
