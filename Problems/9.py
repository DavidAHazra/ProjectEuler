for a in range(1, 10000):
    for b in range(1, 10000):
        c = (a * a + b * b) ** 0.5
        if a + b + c == 1000:
            print(a * b * c)