import os,sys
with open(os.path.join(sys.path[0], "puzzleInput.txt"), "r") as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())

initial = cleanList[0]

code = {}

for e in cleanList[2:]:
  temp = e.split(" -> ")
  code[temp[0]] = temp[1]

initialPairs = {}

for i in range(len(initial) - 1):
  if initial[i:i+2] in initialPairs:
    initialPairs[initial[i:i+2]] += 1
  else:
    initialPairs[initial[i:i+2]] = 1

def iterate(pairs, key):
  newDict = {}
  for e in pairs:
    newPair1 = e[0] + code[e]
    newPair2 = code[e] + e[1]

    if newPair1 in newDict:
      newDict[newPair1] += pairs[e]
    else:
      newDict[newPair1] = pairs[e]
    
    if newPair2 in newDict:
      newDict[newPair2] += pairs[e]
    else:
      newDict[newPair2] = pairs[e]

  return newDict

def countLetters(pairs, start):
  letters = {}
  for e in pairs:
    if e[0] in letters:
      letters[e[0]] += pairs[e]
    else:
      letters[e[0]] = pairs[e]
    if e[1] in letters:
      letters[e[1]] += pairs[e]
    else:
      letters[e[1]] = pairs[e]
  
  #account for doubles, and non doubles on endings
  letters[start[0]] += 1
  letters[start[-1]] += 1

  for e in letters:
    letters[e] = letters[e]//2

  return letters


for i in range(40):
  initialPairs = iterate(initialPairs,code)

letters = countLetters(initialPairs,initial)

letterList = []
for e in letters:
  letterList.append(letters[e])

letterList.sort()

print(letterList[-1] - letterList[0])
