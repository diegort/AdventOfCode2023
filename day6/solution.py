import sys
import re
from math import sqrt, ceil, trunc

def compute_winning_combinations(time, distance):
    discriminator = sqrt(time**2 - 4*distance )

    sol1 = (time + discriminator) / 2
    sol2 = (time - discriminator) / 2
    
    sol1_tunc = trunc(sol1)
    sol2_ceil = ceil(sol2)
    
    if sol1 - sol1_tunc == 0:
        sol1_tunc -= 1
    if sol2_ceil - sol2 == 0:
        sol2_ceil += 1
    
    return sol1_tunc - sol2_ceil + 1

def get_winning_combinations(time, max_distance):
    winning = 0
    for pulse in range(0, time + 1):
        if pulse * (time - pulse) > max_distance:
            winning += 1
    return winning

D = open(sys.argv[1]).read().strip().splitlines()
p1 = 1
p_formula = 1
number_pattern = re.compile(r"\d+")

times, max_distances = [list(map(int, number_pattern.findall(line))) for line in D]

for time, max_distance in zip(times, max_distances):
    p1 *= compute_winning_combinations(time, max_distance)

print(p1)

time, max_distance = [int("".join(number_pattern.findall(line))) for line in D]

print(compute_winning_combinations(time, max_distance))
