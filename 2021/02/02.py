position = {'forward': 0, 'depth': 0}

def process_line(line):
    direction, amount = line.split()
    amount = int(amount)
    if direction == "forward":
        position[direction] += amount
    elif direction == "up":
        position["depth"] -= amount
    elif direction == "down":
        position["depth"] += amount

with open("input.txt") as f:
    for line in f:
        process_line(line)

print(position['forward'] * position['depth'])
