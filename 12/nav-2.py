import math


def rotate(point, angle):
    ox = 0
    oy = 0
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return [qx, qy]


with open("12/nav.txt") as f:
    lines = [x.strip() for x in f.readlines()]

instructions = list(map(lambda x: [x[0], x[1:]], lines))
# I should be using tuples
position = [0, 0]
waypoint = [10, 1]


def move_waypoint(action: str, value: int, waypoint: list):
    if action == "N":
        waypoint[1] += value
    elif action == "S":
        waypoint[1] -= value
    elif action == "E":
        waypoint[0] += value
    elif action == "W":
        waypoint[0] -= value
    else:
        print("ERROR -> move_waypoint")


for inst in instructions:
    action = inst[0]
    value = int(inst[1])
    if action == "L":
        waypoint = rotate((waypoint[0], waypoint[1]), math.radians(value))
    elif action == "R":
        waypoint = rotate((waypoint[0], waypoint[1]), math.radians(-1 * value))
    elif action == "F":
        position[0] += waypoint[0] * value
        position[1] += waypoint[1] * value
    else:
        move_waypoint(action, value, waypoint)


print("Position: ", position)
manhattan_distance = abs(position[0]) + abs(position[1])
print("Manhattan-Distance: ", int(manhattan_distance))

# 83 -> bad
# 5865 -> too low
