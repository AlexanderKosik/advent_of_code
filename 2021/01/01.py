def gen_input():
    yield 199
    yield 200
    yield 208
    yield 210
    yield 200
    yield 207
    yield 240
    yield 269
    yield 260
    yield 263

def compare(base, current):
    if base is None:
        print(current, "(N/A)")
        return False
    return current > base

with open('sim.txt') as f:
    total = 0
    base = None
    for line in f:
        current = int(line)
        cmp = compare(base, current)
        if cmp:
            print(current, "(increased)")
        else:
            print(current, "(decreased)")
        total += cmp
        base = current

print(total)
