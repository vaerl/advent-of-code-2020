with open("8/boot-code.txt") as f:
    code = f.readlines()

operations = []
for op in code:
    operations.append([op, False])

accumulator = 0
index = 0

while True:
    print("Index: ", index)
    value = operations[index][1]
    if value:
        break

    key = operations[index][0]
    op = key.split(" ")[0]
    arg = int(key.split(" ")[1])
    print("Op: ", op)
    print("Arg: ", arg)

    operations[index][1] = True
    if op == "acc":
        accumulator += arg
        index += 1
    elif op == "jmp":
        index += arg
    else:
        index += 1

print("Accumulator: ", accumulator)
