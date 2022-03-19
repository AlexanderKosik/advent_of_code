with open('input.txt') as f:
    total = 0
    for line in f:
        last_part = line.split("|")[1]
        elements = [len(w) for w in last_part.split()]
        total += sum([elements.count(4), elements.count(2), elements.count(3), elements.count(7)])
    print(total)
