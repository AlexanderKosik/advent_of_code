data = [int(x) for x in open('input.txt').read().split(",")]

def fuel_to_distance(position, new_position):
    difference = abs(new_position - position)
    s = sum(range(1, difference+1))
    #print(f"Move from {new_position} to {position}: {s} fuel")
    return s

results = []
max_ = max(data)
min_ = min(data)

for new_position in range(min_, max_+1):
    results.append((sum(fuel_to_distance(x, new_position) for x in data),
        new_position))

#print(results)
print(min(results))
