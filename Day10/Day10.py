with open('puzzleInput.txt') as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())

#find score of line, returns 0 if incomplete
def findScore(line):
  openings = ""
  for e in line:
    if e == "(" or e == "[" or e == "{" or e == "<":
      openings += e
    else:
      if e == ")" and openings[-1] == "(":
        openings = openings[:-1]
      elif e == "]" and openings[-1] == "[":
        openings = openings[:-1]
      elif e == "}" and openings[-1] == "{":
        openings = openings[:-1]
      elif e == ">" and openings[-1] == "<":
        openings = openings[:-1]
      else:
        if e == ")":
          return 3
        elif e == "]":
          return 57
        elif e == "}":
          return 1197
        elif e == ">":
          return 25137
  return 0

total = 0
for line in cleanList:
  total += findScore(line)


def findCompleteScore(line):
  openings = ""
  for e in line:
    if e == "(" or e == "[" or e == "{" or e == "<":
      openings += e
    else:
      if e == ")" and openings[-1] == "(":
        openings = openings[:-1]
      elif e == "]" and openings[-1] == "[":
        openings = openings[:-1]
      elif e == "}" and openings[-1] == "{":
        openings = openings[:-1]
      elif e == ">" and openings[-1] == "<":
        openings = openings[:-1]
      else:
        return 0
  
  #find score for completition:
  total = 0
  for i in reversed(range(len(openings))):
    total *= 5
    if openings[i] == "(":
      total += 1
    elif openings[i] == "[":
      total += 2
    elif openings[i] == "{":
      total += 3
    else:
      total += 4
  
  return total


completeScores = []
for e in cleanList:
  if findCompleteScore(e) == 0:
    pass
  else:
    completeScores.append(findCompleteScore(e))

completeScores.sort()
print(completeScores[(len(completeScores) - 1)// 2])