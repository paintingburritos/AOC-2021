with open('puzzleInput.txt') as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())

stopPoint = cleanList.index("")

points = []
for e in cleanList[:stopPoint]:
  temp = e.split(",")
  for i in range(2):
    temp[i] = int(temp[i])
  points.append(temp)

folds = []
for e in cleanList[(stopPoint+1):]:
  temp = []
  if "x" in e:
    temp.append(0)
  else:
    temp.append(1)
  temp.append(int(e[13:]))
  folds.append(temp)
#axis is either 0 or 1, 0 is x, 1 is y
def fold(points, axis, line):
  newPoints = []
  for e in points:
    if e[axis] <= line:
      if e not in newPoints:
        newPoints.append(e)
    else:
      temp = [e[0], e[1]]
      temp[axis] = temp[axis] - 2 * (temp[axis] - line)
      if temp not in newPoints:
        newPoints.append(temp)    
  return newPoints

# part 1
# first = fold(points, folds[0][0], folds[0][1])
# print(len(first))

#part 2
for e in folds:
  points = fold(points, e[0], e[1])

tempGrid = []
for i in range(10):
  tempGrid.append([])
  for j in range(50):
    tempGrid[-1].append(" ")

for e in points:
  tempGrid[e[1]][e[0]] = "0"

for layer in tempGrid:
  drawLayer = ""
  for e in layer:
    drawLayer += e
  print(drawLayer)

# "PCPHARKL"
