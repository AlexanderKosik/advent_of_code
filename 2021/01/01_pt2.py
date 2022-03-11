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

fn = 'sim.txt'
with open(fn) as f, open(fn) as f2, open(fn) as f3:
    total = 0
    base = None
    i_1 = iter(f)
    i_2 = iter(f2)
    i_3 = iter(f3)
    next(i_2)
    next(i_3)
    next(i_3)
    for a, b, c in zip(i_1, i_2, i_3):
        current = sum(map(int, [a, b, c]))
        cmp = compare(base, current)
        if cmp:
            print(current, "(increased)")
        else:
            print(current, "(decreased)")
        total += cmp
        base = current

print(total)
