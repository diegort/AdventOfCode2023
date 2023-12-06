import sys
import re

def map_category(mappings, val):
    for dest, source, range in mappings:
        if source <= val < source + range:
            return dest + val - source
    else:
        return val

def find_location(mappings, seed):
  value = seed
  for mappings_ in mappings:
    value = map_category(mappings_, value)
  return value

def reverse_map(map_, val):
    for dest, source, range_ in map_:
        if dest <= val < dest + range_:
            return source + val - dest
    else:
        return val

def aggregate_2mappings(map1, map2):
    limits = set([0])
    for dest, source, range_ in map1:
        limits.add(source)
        limits.add(source + range_)
    for dest, source, range_ in map2:
        limits.add(reverse_map(map1, source))
        limits.add(reverse_map(map1, source + range_))
    limits = sorted(limits)

    maps = [map1, map2]
    newmap = []
    for v1, v2 in zip(limits[:-1], limits[1:]):
        w1 = find_location(maps, v1)
        newmap.append((w1, v1, v2 - v1))

    return newmap

def compute_final_mapping(mappings):
  mappings_ = list(mappings.values())
  mapping1 = mappings_[0]
  for mapping2 in mappings_[1:]:
      mapping1 = aggregate_2mappings(mapping1, mapping2)
  return mapping1

D = open(sys.argv[1]).read().strip().replace('  ', ' ').splitlines()
source_and_dest = pattern = re.compile(r'(?P<src>\w+)-to-(?P<dst>\w+).*')

p1 = 0
p2 = 0

almanac = {}

items = 0
seeds = list(map(int, D.pop(0).split(':')[1].strip().split(' ')))
for line in D:
  if line != '':
    if not line[0].isdigit():
      match = pattern.search(line)
      if match:
        current_source = match.groupdict()['src']
        current_dst = match.groupdict()['dst']
        almanac[current_source] = []
    else:
      almanac[current_source].append([int(_) for _ in line.split()])
p1 = min(find_location(list(almanac.values()), seed) for seed in seeds)

p2 = float('inf')
compound_almanac = compute_final_mapping(almanac)
for start, length in zip(seeds[::2], seeds[1::2]):
    for dest, source, range_ in compound_almanac:
        if start <= source < start + length:
            p2 = min(p2, map_category(compound_almanac, source))
        elif source < start and source + range_ - 1 < start + length:
            p2 = min(p2, map_category(compound_almanac, start))

print(p1)
print(p2)