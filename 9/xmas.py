with open("9/xmas.txt") as f:
    xmas = [int(x) for x in f.readlines()]

preamble = xmas[0:25]
data = xmas[25:]
print(preamble)
print(data)


def check(num: int, l: list):
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if l[i] + l[j] == num:
                return True
    return False


invalid = 0

for num in data:
    # check
    if not check(num, preamble):
        print("Number " + str(num) + " not included, breaking!")
        invalid = num
        break
    # append num
    preamble.append(num)
    # remove first from preamble
    preamble.pop(0)


def check_sum(num: int, l: list):
    for i in range(0, len(l)):
        sum = 0
        for j in range(i, len(l)):
            sum += l[j]
            if sum == num:
                res = l[i:j]
                print("Solution: ", min(res) + max(res))
            elif sum > num:
                break


check_sum(invalid, xmas)

# 1762738 -> too low
