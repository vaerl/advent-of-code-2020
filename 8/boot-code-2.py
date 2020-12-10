import copy

with open("8/boot-code.txt") as f:
    code = f.readlines()

operations = []
for op in code:
    operations.append([op.strip(), False])


def check_instructions(instr, change: str):
    accumulator = 0
    index = 0
    while True:
        if index >= len(instr):
            print("Terminated. " + change)
            return True, accumulator
        value = instr[index][1]
        if value:
            print("Loop detected.")
            return False, accumulator

        key = instr[index][0]
        op = key.split(" ")[0]
        arg = int(key.split(" ")[1])

        instr[index][1] = True
        if op == "acc":
            accumulator += arg
            index += 1
        elif op == "jmp":
            index += arg
        else:
            index += 1


def change_instr(l: list, index: int, instr: str):
    res = copy.deepcopy(l)
    line = res[index][0]
    arg = line.split(" ")[1]
    tmp = instr + " " + arg
    res[index][0] = tmp
    return res


nop_to_jmp = []
jmp_to_nop = []

for i in range(len(operations)):
    if operations[i][0].startswith("jmp"):
        tmp = change_instr(operations, i, "nop")
        jmp_to_nop.append(
            {"list": tmp, "change": "Changed jmp to nop at index " + str(i)})
    elif operations[i][0].startswith("nop"):
        tmp = change_instr(operations, i, "jmp")
        nop_to_jmp.append(
            {"list": tmp, "change": "Changed nop to jmp at index " + str(i)})

for x in nop_to_jmp:
    term, acc = check_instructions(x["list"], x["change"])
    if term:
        print("Terminated, acc: ", acc)

for x in jmp_to_nop:
    term, acc = check_instructions(x["list"], x["change"])
    if term:
        print("Terminated, acc: ", acc)
