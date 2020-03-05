def next_collatz(n):
    if n % 2 == 0:
        return n // 2

    return 3 * n + 1


def collatz_sequence(n):
    sequence = [n]
    while sequence[-1] != 1:
        sequence.append(next_collatz(sequence[-1]))

    return sequence


print(max([(num, len(collatz_sequence(num))) for num in range(1, 1000000)], key=lambda c: c[1]))