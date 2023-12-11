import sys

def get_west_cell(current_cell):
    return [current_cell[0], max(0, current_cell[1] - 1)]

def get_east_cell(current_cell, map_width):
    return [current_cell[0], min(map_width, current_cell[1] + 1)]

def get_south_cell(current_cell, map_height):
    return [min(map_height, current_cell[0] + 1), current_cell[1]]

def get_north_cell(current_cell):
    return [max(0, current_cell[0] - 1), current_cell[1]]

def find_candidates(pipes, current_cell, previous_cell):
    cell_type = pipes[current_cell[0]][current_cell[1]]
    candidates = []

    if cell_type == '-':
        candidates = [get_west_cell(current_cell), get_east_cell(current_cell, len(pipes[current_cell[0]]))]

    elif cell_type == '|':
        candidates = [get_north_cell(current_cell), get_south_cell(current_cell, len(pipes))]

    elif cell_type == '7':
        candidates = [get_west_cell(current_cell), get_south_cell(current_cell, len(pipes))]

    elif cell_type == 'F':
        candidates = [get_east_cell(current_cell, len(pipes[current_cell[0]])), get_south_cell(current_cell, len(pipes))]

    elif cell_type == 'L':
        candidates = [get_north_cell(current_cell), get_east_cell(current_cell, len(pipes[current_cell[0]]))]

    elif cell_type == 'J':
        candidates = [get_north_cell(current_cell), get_west_cell(current_cell)]

    if current_cell in candidates:
        candidates.remove(current_cell)
    candidates.remove(previous_cell)

    return candidates

def follow_path(pipes, path):
    while True:
        current_cell = path[-1]
        previous_cell = path[-2]

        candidates = find_candidates(pipes, current_cell, previous_cell)
        if len(candidates) != 0:
            if candidates[0] == path[0]:
                return path
            else:
                path.extend(candidates)
        else:
            return []

def find_loop(pipes, starting_position):
    path = [starting_position]
    # Looking into the right
    if starting_position[1] < len(pipes[starting_position[0]]) - 2:
        candidate_cell = pipes[starting_position[0]][starting_position[1] + 1]
        if candidate_cell == 'J' or candidate_cell == '7' or candidate_cell == '-':
            path.append([starting_position[0], starting_position[1] + 1])
            path1 = follow_path(pipes, path)
            if path1 != []:
                return path1

    # Looking up
    if starting_position[0] > 0:
        candidate_cell = pipes[starting_position[0] - 1][starting_position[1]]
        if candidate_cell == 'F' or candidate_cell == '7' or candidate_cell == '|':
            path.append([starting_position[0] - 1, starting_position[1]])
            path1 = follow_path(pipes, path)
            if path1 != []:
                return path1

    # Looking into the left
    if starting_position[1] > 0:
        candidate_cell = pipes[starting_position[0]][starting_position[1] - 1]
        if candidate_cell == 'L' or candidate_cell == 'F' or candidate_cell == '-':
            path.append([starting_position[0], starting_position[1] - 1])
            path1 = follow_path(pipes, path)
            if path1 != []:
                return path1

    # Looking down
    if starting_position[0] < len(pipes) - 2:
        candidate_cell = pipes[starting_position[0] + 1][starting_position[0]]
        if candidate_cell == 'L' or candidate_cell == 'J' or candidate_cell == '|':
            path.append([starting_position[0], starting_position[1] - 1])
            path1 = follow_path(pipes, path)
            if path1 != []:
                return path1

    return path

def cell_inside_polygon(cell, polygon):
    n = len(polygon)
    inside = False

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        if ((y1 > cell[1]) != (y2 > cell[1])) and (cell[0] < (x2 - x1) * (cell[1] - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside

def calculate_enclosed_cells(loop, pipes):
    enclosed_cells = 0
    for i, line in enumerate(sketch):
        for j, letter in enumerate(line):
            if not [i, j] in loop and cell_inside_polygon([i, j], loop):
                enclosed_cells += 1
    return enclosed_cells

sketch = [list(line.strip()) for line in open(sys.argv[1]).read().strip().splitlines()]
p1 = -1
loop = []
for i, line in enumerate(sketch):
    for j, letter in enumerate(line):
        if letter == 'S':
            starting_position = [i, j]
            loop = find_loop(sketch, [i, j])
            break
    
    if loop != []:
        break

print(int(len(loop) / 2))
print(calculate_enclosed_cells(loop, sketch))