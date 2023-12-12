import sys
import numpy as np

def find_galaxies(universe):
    galaxies = []
    for i, row in enumerate(universe):
        for j, data in enumerate(row):
            if data == '#':
                galaxies.append([i, j])
    return galaxies

source = np.array([list(line.strip()) for line in open(sys.argv[1]).read().strip().splitlines()])
empty_columns = []
empty_rows = []
#Part 1: set this to 2
empty_factor = 1000000

p1 = 0
for index, column in enumerate(source.T):
    if all(item == '.' for item in column):
        empty_columns.append(index)

for index, row in enumerate(source):
    if all(item == '.' for item in row):
        empty_rows.append(index)

galaxies = find_galaxies(source)
for i in range(0, len(galaxies) - 1): # 0..len-2
    for j in range(i + 1, len(galaxies)):
        p1 += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        for column in empty_columns:
            if (galaxies[i][1] < column) != (galaxies[j][1] < column):
                p1 += empty_factor - 1
        for row in empty_rows:
            if (galaxies[i][0] < row) != (galaxies[j][0] < row):
                p1 += empty_factor - 1

print(p1)