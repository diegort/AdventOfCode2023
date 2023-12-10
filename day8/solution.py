import sys
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Función para calcular el MCM de una lista de números
def lcm_list(numbers):
    return reduce(lcm, numbers)

D = open(sys.argv[1]).read().strip().splitlines()

movements = D.pop(0)
secuence_length = len(movements)

D.pop(0)
map = {}
for line in D:
    key, value_temp = [element.strip() for element in line.strip().split('=')]
    value_temp = value_temp.replace('(','').replace(')','')
    destinations = value_temp.split(",")
    valores = {'L': destinations[0].strip(), 'R': destinations[1].strip()}

    map[key.strip()] = valores

paths = []
for key in map.keys():
    if key[2] == 'A':
        current_node = key
        movement_count = 0
        while True:
            movement = movements[movement_count % secuence_length]

            movement_count += 1
            
            if map[current_node][movement][2] == 'Z':
                break
            current_node = map[current_node][movement]
        paths.append(movement_count)

print(lcm_list(paths))
