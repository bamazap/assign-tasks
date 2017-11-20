import numpy as np
from scipy.optimize import linear_sum_assignment
from argparse import ArgumentParser
from tabulate import tabulate

parser = ArgumentParser(description="Assign tasks to people.")

parser.add_argument("csvfile", type=str, help="Path to CSV file.")
parser.add_argument("-r", "--ratio", type=float, default=1,
        help="Scale ranking i to i*geom(r,i)")

args = parser.parse_args()

names = []
tasks = []
rankings = []
with open(args.csvfile) as f:
    first_row = True
    for line in f.readlines():
        row = list(map(lambda c: c.strip(), line.split(",")))
        if first_row:
            tasks = row[1:]
            first_row = False
        else:
            names.append(row[0])
            rankings.append(list(map(lambda r: float(r), row[1:])))

costs = np.array(rankings)
if args.ratio != 1:
    costs = args.ratio**-1 * (1 - np.power(args.ratio, costs))/(1 - args.ratio)
print(costs)
row_ind, col_ind = linear_sum_assignment(costs)

assignments = []
for i, r in enumerate(row_ind):
    c = col_ind[i]
    assignments.append([names[r], tasks[c], rankings[r][c]])

print(tabulate(assignments, headers=["Name", "Task", "Rank"]))
