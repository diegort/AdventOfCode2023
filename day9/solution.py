import sys
def compute_next_value(sequence):
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]

    if not all(diff == 0 for diff in diffs):
        new_item = compute_next_value(diffs)
        return new_item + sequence[-1]
    else:
        return sequence[-1]

def compute_first_value(sequence):
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]

    if not all(diff == 0 for diff in diffs):
        new_item = compute_first_value(diffs)
        return sequence[0] - new_item
    else:
        return sequence[0]

D = [list(map(int, line.split())) for line in open(sys.argv[1]).read().strip().splitlines()]
p1=0
p2=0
for sequence in D:
    p1 += compute_next_value(sequence)
    p2 += compute_first_value(sequence)

print(p1)
print(p2)