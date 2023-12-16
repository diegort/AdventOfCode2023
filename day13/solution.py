import sys
import numpy as np

def get_simetry_line(pattern):
    for i in range(0, len(pattern) - 1):
        simetry = True
        for j in range(0, i + 1):
            if i + j + 1 >= len(pattern):
                break
            item_vs_item = pattern[i - j] == pattern[i +  j + 1]
            np.count_nonzero(item_vs_item == False)
            simetry &= simetry & np.array_equal(pattern[i - j], pattern[i +  j + 1])
        if simetry:
            return i + 1
    return 0

def differences(l, r):
    item_vs_item = l == r
    len(item_vs_item[item_vs_item == False])
    
    return len(item_vs_item[item_vs_item == False])

def get_simetry_line_with_smudge(block: list[str]):
    max_difs = 1
    for i in range(1, len(block)):
        diffs = 0
        for left, right in zip(reversed(block[:i]), block[i:]):
            diffs += differences(left, right)

        if diffs == max_difs:
            return i

    return 0

patterns = [
    np.array([list(row) for row in pattern.strip().split()])
    for pattern in open(sys.argv[1]).read().strip().split('\n\n')
]

p1=0
p2=0
for pattern in patterns:
    counter = get_simetry_line(pattern.T)
    if not counter:
        counter = get_simetry_line(pattern) * 100

    p1 += counter
    
    counter = get_simetry_line_with_smudge(pattern.T)
    if not counter:
        counter = get_simetry_line_with_smudge(pattern) * 100

    p2 += counter

print(p1)
print(p2)