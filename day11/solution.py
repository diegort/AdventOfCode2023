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
expanded_columns = np.array(source)

p1 = 0
added = 0
for index, column in enumerate(source.T):
    if all(item == '.' for item in column):
        expanded_columns = np.insert(expanded_columns, index + added, column, axis=1)
        added += 1

expanded = np.array(expanded_columns)
added = 0
for index, row in enumerate(expanded_columns):
    if all(item == '.' for item in row):
        expanded = np.insert(expanded, index + added, row, axis=0)
        added += 1
        
print(expanded)
galaxies = find_galaxies(source)
for i in range(0, len(galaxies) - 1): # 0..len-2
    for j in range(i + 1, len(galaxies)):
        p1 += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(p1)