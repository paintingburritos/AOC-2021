with open('puzzleInput.txt') as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())
#gamma = most common bit
#epislon least common bit
def findGamma(lines):
  mostCommon = []
  for j in range(len(lines[0])):
    count = 0
    for i in range(len(lines)):
      count += int(lines[i][j])
    
    if count / len(lines) < 0.5:
      mostCommon.append("0")
    else:
      mostCommon.append("1")
  return int("".join(mostCommon),base=2)

def findEpi(lines):
  leastCommon = []
  for j in range(len(lines[0])):
    count = 0
    for i in range(len(lines)):
      count += int(lines[i][j])
    
    if count / len(lines) > 0.5:
      leastCommon.append("0")
    else:
      leastCommon.append("1")
  return int("".join(leastCommon),base=2)

def power(lines):
  return findEpi(lines) * findGamma(lines)


def countMost(lines, pos):
  count0 = 0
  count1 = 0
  for e in lines:
    if int(e[pos]) == 0:
      count0 += 1
    elif int(e[pos]) == 1:
      count1 += 1
    
  if count0 > count1:
    return 0
  else:
    return 1

def countLeast(lines,pos):
  most = countMost(lines,pos)
  if most == 1:
    return 0
  else:
    return 1


def findOxygen(lines):
  tempList = lines[:]
  xpos = 0
  while len(tempList) > 1:
    most = countMost(tempList, xpos)
    for i in reversed(range(len(tempList))):
      if int(tempList[i][xpos]) != most:
        del tempList[i]  
    xpos += 1
    if xpos == len(tempList[0]):
      xpos = 0
    
  return int(tempList[0],base=2)
        
def findCOO(lines):
  tempList = lines[:]
  xpos = 0
  while len(tempList) > 1:
    least = countLeast(tempList, xpos)
    for i in reversed(range(len(tempList))):
      if int(tempList[i][xpos]) != least:
        del tempList[i]  
    xpos += 1
    if xpos == len(tempList[0]):
      xpos = 0
    
  return int(tempList[0],base=2)
        

def findLife(lines):
  return findOxygen(lines) * findCOO(lines)

print(findLife(cleanList))