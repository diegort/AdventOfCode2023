import sys
D = open(sys.argv[1]).read().strip().replace('  ', ' ')
sumMatches = 0
totalCards = 0
copies = {}

for (x, line) in enumerate(D.split('\n')):
  card = int(line.split(':')[0].replace('Card ', ''))
  if copies.get(card) is None:
    copies[card] = 0
  copies[card]+=1
  myNumbers = line.split(':')[1].split('|')[0].strip().split(" ")
  winningNumbers = line.split(':')[1].split('|')[1].strip().split(" ")

  matches = 0
  for number in myNumbers:
    if number in winningNumbers:
      matches += 1
      if copies.get(card+matches) is None:
        copies[card+matches] = 0
      copies[card+matches] += 1*copies[card]
    
  if matches > 0:
    sumMatches += 2**(matches - 1)
    
for v in copies.values():
  totalCards+=v
print(sumMatches)
print(totalCards)