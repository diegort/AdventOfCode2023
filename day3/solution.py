import sys

def get_number_from_coordinates(r, c):
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    return int(s)

grid = open(sys.argv[1]).read().splitlines()
part_numbers_coordinates = set()
p1=0
p2=0

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        gear_candidates = set()
        for dr in range(r - 1, r + 2):
            for dc in range(c - 1, c + 2):
                if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[dr]) or not grid[dr][dc].isdigit():
                    continue
                start = dc
                while start > 0 and grid[dr][start - 1].isdigit():
                    start -= 1
                part_numbers_coordinates.add((dr, start))
                gear_candidates.add((dr, start))

        if grid[r][c] == "*" and len(gear_candidates) == 2:
            print(gear_candidates)
            aux = 1
            for rg, cg in gear_candidates:
                aux *= get_number_from_coordinates(rg, cg)
            p2 += aux

for r, cs in part_numbers_coordinates:
    p1 += get_number_from_coordinates(r, cs)

print(p1)
print(p2)