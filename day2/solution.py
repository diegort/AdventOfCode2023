import sys
import re
D = open(sys.argv[1]).read().strip()
p1 = 0
p2 = 0

pattern = re.compile(r'(?P<red>\d+)\s+red|(?P<blue>\d+)\s+blue|(?P<green>\d+)\s+green')

maxReds = 12
maxGreens = 13
maxBlues = 14

for line in D.split('\n'):
  game = int(line.split(':')[0].replace('Game ', ''))

  reds = 0
  blues = 0
  greens = 0
  minR = -1
  minG = -1
  minB = -1
  possible = True
  for extraction in line.split(':')[1].split(';'):
    matches = re.finditer(pattern, extraction)
    for match in matches:
      if match:
        groups = match.groupdict()
        reds = int(groups['red'] or 0)
        greens = int(groups['green'] or 0)
        blues = int(groups['blue'] or 0)
        
        if reds > maxReds or blues > maxBlues or greens > maxGreens:
          possible = False
        
        minR = max(minR, reds)
        minG = max(minG, greens)
        minB = max(minB, blues)
  
  if possible:
    p1+=game

  p2 += minR*minG*minB

print(p1)
print(p2)