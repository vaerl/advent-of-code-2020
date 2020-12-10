import pandas as pd

dataset = pd.read_csv("2/passwords.csv")
amounts = list(dataset["amount"])
chars = list(dataset["letter"])
passwords = list(dataset["password"])

valid = 0

# check valid number of passwords: between min and max occurrences of the character
for i in range(len(dataset)):
    pos = amounts[i].split("-")
    min = int(pos[0])
    max = int(pos[1])
    char = chars[i]
    password = passwords[i]

    search = ""
    for c in password:
        if c == char:
            search += c

    if len(search) >= min and len(search) <= max:
        valid += 1

print(valid)

valid = 0

# check valid number of passwords: exactly one index must
for i in range(len(dataset)):
    pos = amounts[i].split("-")
    a = int(pos[0])
    b = int(pos[1])
    char = chars[i]
    password = passwords[i]

    if bool(password[a-1] == char) ^ bool(password[b-1] == char):
        valid += 1

print(valid)
