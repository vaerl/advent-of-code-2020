import re

with open("4/passports.txt") as f:
    txt = f.readlines()

valid = 0

attributes = [
    ["byr", False],
    ["iyr", False],
    ["eyr", False],
    ["hgt", False],
    ["hcl", False],
    ["ecl", False],
    ["pid", False],
]


def reset():
    for attribute in attributes:
        attribute[1] = False
    print("RESET: ", attributes)


# first
for line in txt:
    if line == '\n':
        reset()
    else:
        print("Line: ", line)
        elements = line.split(" ")
        for field in elements:
            attr = field.split(":")[0]
            for attribute in attributes:
                if attribute[0] == attr:
                    attribute[1] = True
                    print("Update: ", attribute)
        print("RESULT: ", attributes)
        update = True
        for attribute in attributes:
            if not attribute[1]:
                update = False
                print("INVALID")
                break
        if update:
            print("VALID")
            valid += 1
            reset()


print("length: ", len(txt))
print(valid)


# second
def byr(year):
    if len(year) < 4:
        return False
    year = int(year)
    return year >= 1920 and year <= 2002


def iyr(year):
    if len(year) < 4:
        return False
    year = int(year)
    return year >= 2010 and year <= 2020


def eyr(year):
    if len(year) < 4:
        return False
    year = int(year)
    return year >= 2020 and year <= 2030


def pid(year: str):
    return len(year) == 9


def ecl(col: str):
    x = col in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return x


def hcl(col: str):
    x = re.match("#([a-f]|[0-9]){6}", col)
    return not x == None


def hgt(hgt: str):
    if "cm" in hgt:
        hgt = hgt[:-2]
        hgt = int(hgt)
        return hgt >= 150 and hgt <= 193
    elif "in" in hgt:
        hgt = hgt[:-2]
        hgt = int(hgt)
        return hgt >= 59 and hgt <= 76
    else:
        return False


value = {"byr": byr,
         "iyr": iyr,
         "eyr": eyr,
         "hgt": hgt,
         "hcl": hcl,
         "ecl": ecl,
         "pid": pid,
         }


valid = 0
reset()

for line in txt:
    if line == '\n':
        reset()
    else:
        print("Line: ", line)
        elements = line.split(" ")
        for field in elements:
            field = field.split(":")
            attr = field[0]
            val = field[1]
            for attribute in attributes:
                if attribute[0] == attr:
                    attribute[1] = value[attr](val.strip())
                    print("Value:", val)
                    print("Update: ", attribute)
        print("RESULT: ", attributes)
        update = True
        for attribute in attributes:
            if not attribute[1]:
                update = False
                print("INVALID")
                break
        if update:
            print("VALID")
            valid += 1
            reset()


print("length: ", len(txt))
print(valid)
