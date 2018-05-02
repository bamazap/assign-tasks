import numpy as np
from scipy.optimize import linear_sum_assignment
from argparse import ArgumentParser
from tabulate import tabulate

parser = ArgumentParser(description="Assign tasks to people.")
parser.add_argument("tsvfile", type=str, help="Path to TSV file.")
parser.add_argument("-r", "--ratio", type=float, default=1,
        help="Scale ranking k to 1/r * (1 + r + r**2 + ... + r**(k-1))")
args = parser.parse_args()

def parse_tsv_line(line):
    return [c.strip() for c in line.split("\t")]

names = []
tasks = []
rankings = []
with open(args.tsvfile) as f:
    tasks = parse_tsv_line(f.readline())[1:]
    for line in f.readlines():
        row = parse_tsv_line(line) 
        names.append(row[0])
        rankings.append([float(r) for r in row[1:]])

costs = np.array(rankings)
if args.ratio != 1:
    costs = args.ratio**-1 * (1 - np.power(args.ratio, costs))/(1 - args.ratio)
row_ind, col_ind = linear_sum_assignment(costs)

assignments = []
for i, r in enumerate(row_ind):
    c = col_ind[i]
    assignments.append([names[r], tasks[c], rankings[r][c]])

print(tabulate(assignments, headers=["Name", "Task", "Rank"]))
