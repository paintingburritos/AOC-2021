with open('puzzleInput.txt') as pInput:
  lines = pInput.readlines()
instructions = []
for e in lines:
  instructions.append(e.split())

#part 1
posx1 = 0
posy1 = 0
for e in instructions:
  if e[0] == "forward":
    posx1 += int(e[1])
  elif e[0] == "down":
    posy1 += int(e[1])
  elif e[0] == "up":
    posy1 -= int(e[1])
print(posx1*posy1)


posx2 = 0
posy2 = 0
aim = 0
for e in instructions:
  if e[0] == "forward":
    posx2 += int(e[1])
    posy2 += aim*int(e[1])
  elif e[0] == "down":
    aim += int(e[1])
  elif e[0] == "up":
    aim -= int(e[1])
    

  
print(posx2)
print(posy2)
print(posy2*posx2)