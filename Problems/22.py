import string
import os

with open(os.path.join(os.getcwd(), "..", "ProblemData", "22_names.txt"), 'r') as name_file:
    print(sum((index + 1) * sum(string.ascii_uppercase.index(letter) + 1 for letter in name)
              for index, name in enumerate(sorted([name[1:-1] for name in name_file.read().split(',')]))))
