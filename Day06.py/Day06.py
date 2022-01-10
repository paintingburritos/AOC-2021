with open('puzzleInput.txt') as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())
splitList = cleanList[0].split(",")
finalList = []
for e in splitList:
  finalList.append(int(e))

def iterateBad(fish):
  newList = []
  for e in fish:
    if e == 0:
      newList.append(6)
      newList.append(8)
    else:
      newList.append(e-1)
  return newList

countedFish = []
for i in range(9):
  countedFish.append([i,0])

for e in finalList:
  countedFish[e][1] += 1


def iterateGood(fish):
  newList = []
  for i in range(9):
    newList.append([i,0])

  for e in fish:
    if e[0] == 0:
      newList[6][1] += e[1]
      newList[8][1] += e[1]
    else:
      newList[e[0]-1][1] += e[1]
  return newList
for i in range(256):
  countedFish = iterateGood(countedFish)

total = 0
for e in countedFish:
  total += e[1]

print(total)