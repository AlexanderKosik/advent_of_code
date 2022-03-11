with open('s.txt') as f, open('s.txt') as f_2, open('s.txt') as f_3:
    total = 0
    base = None
    l = list(range(100))
    i_1 = iter(f)
    i_2 = iter(f_2)
    i_3 = iter(f_3)
    next(i_2)
    next(i_3)
    next(i_3)
    for a, b, c in zip(i_1, i_2, i_3):
        print(a, b, c)
