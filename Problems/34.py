import math

n = 3
running_total = 0
while True:
    if n == sum(math.factorial(int(i)) for i in str(n)):
        running_total += n
        print(running_total)

    n += 1
