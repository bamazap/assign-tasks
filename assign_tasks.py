import numpy as np
from scipy.optimize import linear_sum_assignment
from argparse import ArgumentParser
from tabulate import tabulate

parser = ArgumentParser(description="Assign tasks to people.")

parser.add_argument("csvfile", type=str, help="Path to CSV file.")

args = parser.parse_args()

names = []
tasks = []
data = []
with open(args.csvfile) as f:
    first_row = True
    for line in f.readlines():
        row = list(map(lambda c: c.strip(), line.split(",")))
        if first_row:
            tasks = row[1:]
            first_row = False
        else:
            names.append(row[0])
            data.append(list(map(lambda i: float(i), row[1:])))

data = np.array(data)
row_ind, col_ind = linear_sum_assignment(data)

assignments = []
for i, r in enumerate(row_ind):
    c = col_ind[i]
    assignments.append([names[r], tasks[c], data[r][c]])

print(tabulate(assignments, headers=["Name", "Task", "Rank"]))
