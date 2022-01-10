import os,sys
with open(os.path.join(sys.path[0], "puzzleInput.txt"), "r") as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())
tempList1 = []
for e in cleanList:
  tempList1.append(e.split(" -> "))
tempList2 = []
for e in tempList1:
  tempList2.append([])
  for coord in e:
    tempList2[-1].append(coord.split(","))
finalList = []
for line in tempList2:
  finalList.append([])
  for coord in line:
    finalList[-1].append([])
    for num in coord:
      finalList[-1][-1].append(int(num))
    
grid = []
for i in range(1000):
  grid.append([])
  for j in range(1000):
    grid[-1].append(0)

def lineCoord(coord1,coord2):
  points = []
  if coord1[0] == coord2[0]:
    for i in range(abs(coord2[1]-coord1[1])+1):
      if coord1[1] > coord2[1]:
        points.append((coord1[0],coord2[1]+i))
      else:
        points.append((coord1[0],coord1[1]+i))
  elif coord1[1] == coord2[1]:
    for i in range(abs(coord2[0]-coord1[0])+1):
      if coord1[0] > coord2[0]:
        points.append((coord2[0]+i,coord1[1]))
      else:
        points.append((coord1[0]+i,coord1[1]))
  
  #part 2
  else:
    for i in range(abs(coord2[0]-coord1[0])+1):
      #BL to TR C1
      if coord1[0] < coord2[0] and coord1[1] < coord2[1]:
        points.append((coord1[0]+i,coord1[1]+i))
      #BL to TR C2
      elif coord2[0] < coord1[0] and coord2[1] < coord1[1]:
        points.append((coord2[0]+i,coord2[1]+i))
      #TL to BR c1
      elif coord1[0] < coord2[0] and coord2[1] < coord1[1]:
        points.append((coord1[0]+i,coord1[1]-i))
      else: #TL to BR c2
        points.append((coord2[0]+i,coord2[1]-i))
  return points

for line in finalList:
  for point in lineCoord(line[0],line[1]):
    grid[point[1]][point[0]] += 1
count = 0
for layer in grid:
  for e in layer:
    if e >= 2:
      count += 1

print(count)

