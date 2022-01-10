import os,sys
with open(os.path.join(sys.path[0], "puzzleInput.txt"), "r") as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())
splitList = cleanList[0].split(",")
finalList = []
for e in splitList:
  finalList.append(int(e))



def part1(posistions):
  maxValue = max(posistions)
  fuels = []

  for i in range(maxValue + 1):
    tempSum = 0
    for e in posistions:
      tempSum += abs(i-e)
    fuels.append(tempSum)
  return fuels

def part2(posistions):
  maxValue = max(posistions)
  fuels = []

  for i in range(maxValue + 1):
    tempSum = 0
    for e in posistions:
      a = abs(i-e)
      tempSum += a * (a+1) / 2
    fuels.append(tempSum)
  return fuels

print(min(part2(finalList)))
