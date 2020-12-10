with open("7/rules.txt") as f:
    rules = f.readlines()


def find_rule(color: str):
    for rule in rules:
        if rule.startswith(color):
            return rule


def extract_info(rule: str):
    bags = rule.split("contain")[1].strip().split(",")
    res = []
    for bag in bags:
        bag = bag.strip().split(" ")
        if bag[0] == "no":
            continue
        res.append({bag[1] + " " + bag[2]: int(bag[0])})
    return res


def check(color):
    print("Color: ", color)
    bags = extract_info(find_rule(color))
    print("Bags: ", bags)
    if len(bags) < 1:
        return 0
    res = 0
    for bag in bags:
        res += list(bag.values())[0] + list(bag.values()
                                            )[0] * check(list(bag.keys())[0])
        print("Res: " + str(color), res)
    return res


print(check("shiny gold"))

# 4758 -> too low
# 10393 -> too high
