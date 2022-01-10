with open('puzzleInput.txt') as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())

ballsTemp = cleanList[0].split(",")
balls = []
for e in ballsTemp:
  balls.append(int(e))

boards = []

for i in range((len(cleanList)-1)//6):
  tempBoard = []
  for j in range(5):
    tempList = cleanList[6*i+j+2].split()
    tempIntList = []
    for e in tempList:
      tempIntList.append(int(e))
    tempBoard.append(tempIntList)
  boards.append(tempBoard)


#checks for win on board, given a list of called balls
def checkWin(board, called):
  scoreSheet = []
  for i in range(5):
    scoreSheet.append([])
    for j in range(5):
      scoreSheet[-1].append(0)
  
  for i in range(5):
    for j in range(5):
      if board[i][j] in called:
        scoreSheet[i][j] = 1
  
  win = False
  # #diag
  # diagWinTR = True
  # for i in range(5):
  #   if scoreSheet[i][i] != 1:
  #     diagWinTR = False
  
  # diagWinTL = True
  # for i in range(5):
  #   if scoreSheet[i][4-i] != 1:
  #     diagWinTL = False

  # if diagWinTR or diagWinTL:
  #   win = True

  #hor
  for layer in scoreSheet:
    if 0 in layer:
      pass
    else:
      win = True
  
  #vert
  for i in range(5):
    temp = []
    for j in range(5):
      temp.append(scoreSheet[j][i])
    
    if 0 in temp:
      pass
    else:
      win = True
  
  if win:
    score = 0
    for i in range(5):
      for j in range(5):
        if scoreSheet[i][j] == 0:
          score += board[i][j]

    score *= called[-1]
    return score
  else:
    return 0

#part 1 calls
# running = True
# calls = []
# pos = 0
# while running:
#   calls.append(balls[pos])
#   pos += 1
#   for e in boards:
#     test = checkWin(e, calls)
#     if test != 0:
#       print(test)
#       running = False
  
#part 2 calls
running = True
wonBoards = []
calls = []

pos = 0
while running:
  calls.append(balls[pos])
  pos += 1
  for e in boards:
    test = checkWin(e, calls)
    if test != 0:
      wonBoards.append(e)
      boards.remove(e)

  if len(boards) == 0:
    break

print(checkWin(wonBoards[-1],calls))  


  