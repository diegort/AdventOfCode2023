import sys

D = open(sys.argv[1]).read().strip().splitlines()
p1 = 0

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

current_node = 'AAA'
while True:
    movement = movements[p1 % secuence_length]

    p1 += 1
    
    if map[current_node][movement] == 'ZZZ':
        break
    current_node = map[current_node][movement]

print(p1)