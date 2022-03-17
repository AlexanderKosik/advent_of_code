with open('input.txt') as f:
    pop = [int(x) for x in next(f).split(',')]
    print("Init", pop)
    for _ in range(80):
        new_pop = []
        for idx, value in enumerate(pop):
            if value -1 < 0:
                value = 6
                new_pop.append(8)
            else:
                value -= 1
            pop[idx] = value
        pop.extend(new_pop)
        print(f"Day {_}:", len(pop))

    print(len(pop))

            
