numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred",
    200: "two hundred",
    300: "three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred",
    1000: "one thousand"
}


def number_string(n):
    if n in numbers:
        return numbers[n]

    current = int(str(n)[0] + "0" * (len(str(n)) - 1))
    if current not in numbers:
        print("{0} - {1} not in numbers".format(n, current))
        exit(-1)

    else:
        if current < 100:
            return numbers[current] + " " + number_string(int(str(n)[1:]))

        else:
            return numbers[int(str(current)[0])] + " hundred and " + number_string(int(str(n)[1:]))


print(len("".join(number_string(i).replace(" ", "") for i in range(1, 1001))))