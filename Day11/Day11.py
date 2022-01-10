import copy
import os,sys
with open(os.path.join(sys.path[0], "puzzleInput.txt"), "r") as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())

integerList = []
for layer in cleanList:
  integerList.append([])
  for e in layer:
    integerList[-1].append(int(e))

def blankBoard(x,y):
  temp = []
  for i in range(y):
    temp.append([])
    for j in range(x):
      temp[-1].append(0)
  return temp



class Board:
  def __init__(self, state):
    self.state = state
    self.flashes = 0
    self.boardY = len(state)
    self.boardX = len(state[0])
  
  def __str__(self):
    finalString = ""
    for layer in self.state:
      for e in layer:
        finalString += str(e)
      finalString += "\n"
    finalString += "Flashes: " + str(self.flashes)
    return finalString

  def iterate(self):
    # Step 1
    for y in range(self.boardY):
      for x in range(self.boardX):
        self.state[y][x] += 1
    
    flashBoard = blankBoard(self.boardX, self.boardY)
    # Step 2
    running = True
    while running:
      oldFlash = copy.deepcopy(flashBoard)
      for y in range(self.boardY):
        for x in range(self.boardX):
          if self.state[y][x] > 9 and flashBoard[y][x] == 0:
            flashBoard[y][x] = 1
            self.flashes += 1
            borderL,borderR,borderD,borderU = True, True, True, True
            if x == 0:
              borderL = False
            if y == 0:
              borderU = False
            if x == self.boardX - 1:
              borderR = False
            if y == self.boardY - 1:
              borderD = False
            if borderU:
              self.state[y-1][x] += 1
              if borderL:
                self.state[y-1][x-1] += 1
              if borderR:
                self.state[y-1][x+1] += 1
            if borderD:
              self.state[y+1][x] += 1
              if borderL:
                self.state[y+1][x-1] += 1
              if borderR:
                self.state[y+1][x+1] += 1
            if borderL:
              self.state[y][x-1] += 1
            if borderR:
              self.state[y][x+1] += 1
      if flashBoard == oldFlash:
        running = False
    # step 3
    for y in range(self.boardY):
      for x in range(self.boardX):
        if self.state[y][x] > 9:
          self.state[y][x] = 0
          

octopi = Board(copy.deepcopy(integerList))
octopi2 = Board(copy.deepcopy(integerList))

for i in range(100):
  octopi.iterate()

print(octopi.flashes)


stepCount = 0
while True:
  initial = octopi2.flashes
  octopi2.iterate()
  stepCount += 1
  if octopi2.flashes - initial == (len(octopi2.state) * len(octopi2.state[0])):
    break

print(stepCount)