import copy


with open("11/seats.txt") as f:
    lines = [x.strip() for x in f.readlines()]


seats = []
for line in lines:
    tmp = []
    for char in line:
        tmp.append(char)
    seats.append(tmp)


def update(tmp: list, org: list, i: int, j: int):
    current = tmp[i][j]
    adjacent = []

    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x < 0 or y < 0 or x > len(tmp) - 1 or y > len(tmp[0]) - 1 or (x == i and y == j):
                continue
            adjacent.append(org[x][y])

    print("Adjacent for (" + str(i) + ", " + str(j) + ") -> " +
          str(current)+": ", adjacent)

    if current == "L":
        if not "#" in adjacent:
            tmp[i][j] = "#"
            return True
    elif current == "#":
        x = [x for x in adjacent if x == "#"]
        if len(x) > 3:
            tmp[i][j] = "L"
            return True
    return False


while True:
    tmp = copy.deepcopy(seats)
    change = False
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == ".":
                continue
            else:
                if update(tmp, seats, i, j):
                    change = True
    if not change:
        break
    seats = copy.deepcopy(tmp)

print("Change is: ", change)
print("Seats: ", seats)

count = 0
for row in seats:
    for seat in row:
        if seat == "#":
            count += 1

print("Occupied seats: ", count)
