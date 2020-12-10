with open("5/passes.txt") as f:
    passes = f.readlines()

max = -1

rows = list(range(0, 128))
cols = list(range(0, 8))

seats = []


for p in passes:
    p = p.strip()
    for char in p:
        if char == "F":
            rows = rows[:len(rows)//2]
        elif char == "B":
            rows = rows[len(rows)//2:]
        elif char == "R":
            cols = cols[len(cols)//2:]
        elif char == "L":
            cols = cols[:len(cols)//2]
    res = rows[0] * 8 + cols[0]
    seats.append(res)
    if res > max:
        max = res
    rows = list(range(0, 128))
    cols = list(range(0, 8))

print("Result: ", max)
# 2 -> I just looked at the data
print("Seats: ", sorted(seats))
