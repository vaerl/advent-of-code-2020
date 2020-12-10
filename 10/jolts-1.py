with open("10/jolts.txt") as f:
    jolts = sorted([int(x.strip()) for x in f.readlines()])

print(jolts)
jolts.insert(0, 0)
jolts.append(jolts[len(jolts) - 1] + 3)
print(jolts)

one = 0
three = 0

for i in range(1, len(jolts)):
    res = jolts[i] - jolts[i-1]
    if res == 1:
        one += 1
    elif res == 3:
        three += 1

print("Result: ", one * three)
