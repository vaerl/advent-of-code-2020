with open("7/rules.txt") as f:
    rules = f.readlines()


def get_containers(color: str):
    res = []
    for rule in rules:
        if color in rule:
            rule = rule.strip().split(" ")
            res.append(rule[0] + " " + rule[1])
    return res


# def check(color: str):
#     result = list(set(get_containers(color)))
#     print("Res: ", result)
#     if len(result) == 0:
#         return 0
#     else:
#         num = 0
#         for res in result:
#             if res == color:
#                 num -= 1
#                 continue
#             num += check(res)
#         return len(result) + num

def check(color: str):
    print("Color: ", color)
    result = list(set(get_containers(color)))
    result.remove(color)
    print("Result: ", result)

    if len(result) < 1:
        return []

    temp = []
    for res in result:
        temp.extend(set(check(res)))
    result.extend(temp)
    return list(set(result))


res = check("shiny gold")
print("Result: ", len(res))
