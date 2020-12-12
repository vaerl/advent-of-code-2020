with open("12/nav.txt") as f:
    lines = [x.strip() for x in f.readlines()]

instructions = list(map(lambda x: [x[0], x[1:]], lines))
direction = "E"
position = [0, 0]


def move(action: str, value: int):
    if action == "N":
        position[1] += value
    elif action == "S":
        position[1] -= value
    elif action == "E":
        position[0] += value
    elif action == "W":
        position[0] -= value
    else:
        print("ERROR -> Move")


def change_direction(direction: str, value: int):
    degrees = 0
    if direction == "N":
        degrees = 0
    elif direction == "S":
        degrees = 180
    elif direction == "E":
        degrees = 90
    elif direction == "W":
        degrees = 270

    degrees = (degrees + value) % 360

    if degrees == 0:
        return "N"
    elif degrees == 180:
        return "S"
    elif degrees == 90:
        return "E"
    elif degrees == 270:
        return "W"


for inst in instructions:
    action = inst[0]
    value = int(inst[1])
    if action == "L":
        direction = change_direction(direction, -1 * value)
    elif action == "R":
        direction = change_direction(direction, value)
    elif action == "F":
        move(direction, value)
    else:
        move(action, value)


print("Position: ", position)
manhattan_distance = abs(position[0]) + abs(position[1])
print("Manhattan-Distance: ", manhattan_distance)
