with open('puzzleInput.txt') as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())

#part 1
totalRisk = 0
lowPoints = []
for y in range(len(cleanList)):
  for x in range(len(cleanList[0])):
    lowPoint = True
    if x < len(cleanList[0]) - 1:
      if int(cleanList[y][x]) >= int(cleanList[y][x+1]):
        lowPoint = False
    if x > 0:
      if int(cleanList[y][x]) >= int(cleanList[y][x-1]):
        lowPoint = False
    if y > 0:
      if int(cleanList[y][x]) >= int(cleanList[y-1][x]):
        lowPoint = False
    if y < len(cleanList) - 1:
      if int(cleanList[y][x]) >= int(cleanList[y+1][x]):
        lowPoint = False
    if lowPoint:
      totalRisk += int(cleanList[y][x]) + 1
      lowPoints.append((x,y))


cleanList.insert(0, "")
cleanList.append("")
for i in range(len(cleanList[1])+2):
  cleanList[-1] += "9"
  cleanList[0] += "9"
for i in range(len(cleanList) - 2):
  cleanList[i+1] = "9" + cleanList[i+1] + "9"




# returns coordinates of basin from coords of a given point
def findBasin(x,y, floor):
  if floor[y][x] == "9":
    return 0
  while True:
    if floor[y][x] > floor[y+1][x]:
      y += 1
    elif floor[y][x] > floor[y-1][x]:
      y -= 1
    elif floor[y][x] > floor[y][x+1]:
      x += 1
    elif floor[y][x] > floor[y][x-1]:
      x -= 1
    else:
      return (x,y)


basinSizes = dict()

for y in range(len(cleanList)):
  for x in range(len(cleanList[0])):
    point = findBasin(x,y,cleanList)
    if point == 0:
      pass
    else:
      if point in basinSizes:
        basinSizes[point] += 1
      else:
        basinSizes[point] = 1

sizes = []
for e in basinSizes:
  sizes.append(basinSizes[e])

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
