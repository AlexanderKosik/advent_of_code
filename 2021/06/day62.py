with open('input.txt') as f:
    pop = [int(x) for x in next(f).split(',')]
    print("Init", pop)
    pop = {
        8: pop.count(8),
        7: pop.count(7),
        6: pop.count(6),
        5: pop.count(5),
        4: pop.count(4),
        3: pop.count(3),
        2: pop.count(2),
        1: pop.count(1),
        0: pop.count(0)
    }
    
    for day in range(256):
        new_pop = pop[0]
        for x in range(0, 8):
            pop[x] = pop[x+1]
        pop[8] = new_pop
        pop[6] += new_pop

        print(f"Day: {day}", sum(pop.values()))



            
