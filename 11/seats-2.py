import copy


with open("11/seats.txt") as f:
    lines = [x.strip() for x in f.readlines()]


seats = []
for line in lines:
    tmp = []
    for char in line:
        tmp.append(char)
    seats.append(tmp)


def valid(i: int, j: int, l: list):
    return i >= 0 and j >= 0 and i < len(l) and j < len(l[0])


def inc(x: int):
    return x + 1


def dec(x: int):
    return x - 1


def id(x: int):
    return x


def direction(i: int, j: int, row, col, l: list):
    x = row(i)
    y = col(j)

    res = None

    while valid(x, y, l):
        current = l[x][y]
        if current == "#" or current == "L":
            res = current
            break
        else:
            x = row(x)
            y = col(y)

    if res == None:
        res = "."
    return res


def update(tmp: list, org: list, i: int, j: int):
    current = tmp[i][j]
    adjacent = []

    adjacent.append(direction(i, j, dec, dec, org))
    adjacent.append(direction(i, j, dec, id, org))
    adjacent.append(direction(i, j, dec, inc, org))
    adjacent.append(direction(i, j, id, dec, org))
    adjacent.append(direction(i, j, id, inc, org))
    adjacent.append(direction(i, j, inc, dec, org))
    adjacent.append(direction(i, j, inc, id, org))
    adjacent.append(direction(i, j, inc, inc, org))

    if current == "L":
        if not "#" in adjacent:
            tmp[i][j] = "#"
            print("Change to #")
            return True
    elif current == "#":
        x = [x for x in adjacent if x == "#"]
        if len(x) >= 5:
            tmp[i][j] = "L"
            print("Change to L")
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

count = 0
for row in seats:
    for seat in row:
        if seat == "#":
            count += 1

print("Occupied seats: ", count)

# 2424 -> too high
