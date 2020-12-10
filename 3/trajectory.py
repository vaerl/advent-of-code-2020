# open file
with open("3/map.txt") as f:
    map = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
map = [x.strip() for x in map]


def check_trees(right: int, down: int):
    col = 0
    trees = 0
    i = 0
    while i < len(map):
        if map[i][col] == "#":
            trees += 1
        col += right
        col = col % len(map[i])
        i += down
    return trees


a = check_trees(1, 1)
b = check_trees(3, 1)
c = check_trees(5, 1)
d = check_trees(7, 1)
e = check_trees(1, 2)


print("number of trees for 1, 1: ", a)
print("number of trees for 3, 1: ", b)
print("number of trees for 5, 1: ", c)
print("number of trees for 7, 1: ", d)
print("number of trees for 1, 2: ", e)

print("Product: ",  a*b*c*d*e)
