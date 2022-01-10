with open('puzzleInput.txt') as pInput:
  lines = pInput.readlines()
cleanList = []
for e in lines:
  cleanList.append(e.strip())

#part 1
temp1 = []
for e in cleanList:
  temp1.append(e.split("|"))
temp2 = []
part2list = []
for e in temp1:
  temp2.append(e[1].split())
  part2list.append([e[0].split(),e[1].split()])

count = 0
for e in temp2:
  for f in e:
    if len(f) in (2,3,4,7):
      count += 1
def match(str1,str2):
  matches = []
  for e in str1:
    for f in str2:
      if e == f:
        matches.append(e)
  return matches

def diff(str1,str2):
  matches = match(str1,str2)
  different = []
  for e in str1:
    if e not in matches:
      different.append(e)

  for e in str2:
    if e not in matches:
      different.append(e)
      
  return different
  
def occurOnce(letters):
  count = dict()
  for e in letters:
    if e in count:
      count[e] += 1
    else:
      count[e] = 0
  
  once = []
  for e in count:
    if count[e] == 0:
      once.append(e)

  return once

def findKey(scrambled):
  scrambled.sort(key=len)
  # 0, 1, 2,    3,4,5,       6,7,8     9
  # 1, 7, 4, 5seg(2,5,3), 6seg(0,6,9), 8
  key = dict()
  #find key for a:
  key["a"] = diff(scrambled[0],scrambled[1]) # found
  #2,5,3
  matchThree = match(match(scrambled[3],scrambled[4]), scrambled[5])
  #pairs
  key["c"] = diff(matchThree, match(scrambled[3],scrambled[4])) + diff(matchThree, match(scrambled[4],scrambled[5])) + diff(matchThree, match(scrambled[3],scrambled[5])) 
  key["f"] = diff(matchThree, match(scrambled[3],scrambled[4])) + diff(matchThree, match(scrambled[4],scrambled[5])) + diff(matchThree, match(scrambled[3],scrambled[5])) 
  #singles
  key["b"] = occurOnce(scrambled[3]+scrambled[4]+scrambled[5])
  key["e"] = occurOnce(scrambled[3]+scrambled[4]+scrambled[5])
  #0,6,9:
  key["c"] = match(diff(scrambled[6],scrambled[7]) + list(diff(scrambled[7],scrambled[8])[0]), key["c"]) # found
  key["f"] = diff(key["c"],key["f"]) # found
  key["d"] = diff(scrambled[6],scrambled[7]) + list(diff(scrambled[7],scrambled[8])[0])
  key["e"] = match(diff(scrambled[6],scrambled[7]) + list(diff(scrambled[7],scrambled[8])[0]), key["e"]) # found
  key["b"] = diff(key["b"],key["e"]) # found
  key["d"] = diff(diff(key["d"],key["c"]), key["e"]) #found
  found = []
  for e in key:
    found.append(key[e][0])  
  key["g"] = ["a","b","c","d","e","f","g"]
  for e in found:
    if e in key["g"]:
      key["g"].remove(e) #found
  
  flippedKey = dict()
  for e in key:
    flippedKey[key[e][0]] = e
  return flippedKey


def findNum(code, scramb):
  decoder = {
  "abcefg":0,
  "cf":1,
  "acdeg":2,
  "acdfg":3,
  "bcdf":4,
  "abdfg":5,
  "abdefg":6,
  "acf":7,
  "abcdefg":8,
  "abcdfg":9
}

  key = findKey(scramb)
  
  unscrambled = []
  for e in code:
    unscrambled.append("")
    for letter in e:
      unscrambled[-1] += key[letter]
    unscrambled[-1] = sorted(unscrambled[-1])
    unscrambled[-1] = "".join(unscrambled[-1])

  total = 0
  for i in range(4):
    total += decoder[unscrambled[i]] * (10**(3-i))  
  return total



runningTotal = 0

for e in part2list:
  runningTotal += findNum(e[1],e[0])

print(runningTotal)

