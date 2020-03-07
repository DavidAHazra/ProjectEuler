import os
with open(os.path.join(os.getcwd(), "..", "ProblemData", "67_triangle.txt"), 'r') as triangle_file:
    num_rows = [[int(number) for number in line] for line in [line.split(" ")
                                                              for line in triangle_file.read().split("\n")[:-1]]]

    for row_index in range(len(num_rows) - 1, 0, -1):
        num_rows = num_rows[:row_index - 1] + \
                   [[num_rows[row_index - 1][index] +
                     max(num_rows[row_index][index], num_rows[row_index][index + 1])
                     for index in range(len(num_rows[row_index - 1]))]]

    print(num_rows[0][0])


