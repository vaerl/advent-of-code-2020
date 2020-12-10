with open("10/jolts.txt") as f:
    jolts = sorted([int(x.strip()) for x in f.readlines()])

jolts.insert(0, 0)
jolts.append(jolts[len(jolts) - 1] + 3)

comb = []
cache_comb = {}
cache_paths = {}
accepted = [1, 2, 3]


def get_comb(current: int, l: list):
    print("Checking combinations for: ", current)
    if str(current) in cache_comb:
        return cache_comb[str(current)]
    else:
        res = []
        for num in accepted:
            if current + num in l:
                res.append(Tree(current + num, l))
        cache_comb[str(current)] = res
        return res


class Tree(object):
    "Generic tree node."

    def __init__(self, value: int, l: list):
        self.value = value
        self.children = get_comb(value, l)

    def __repr__(self):
        return str(self.value)

    def paths(self):
        if not self.children:  # checks if array is empty
            return 1
        paths = 0
        for child in self.children:
            if str(child) in cache_paths:
                res = cache_paths[str(child)]
            else:
                res = child.paths()
            cache_paths[str(child)] = res
            paths += res
        return paths


tree = Tree(jolts[0], jolts)
paths = tree.paths()
print(paths)
