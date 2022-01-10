import os,sys
with open(os.path.join(sys.path[0], "puzzleInput.txt"), "r") as pInput:
  lines = pInput.readlines()
lines = [int(i) for i in lines]

# depths: List of depths
# windowLen: Length of window being summed
def windowIncrease(depths,windowLen):
  count = 0
  for i in range(len(depths)-windowLen):
    sumA = 0
    sumB = 0
    for j in range(windowLen):
      sumA += depths[i+j]
      sumB += depths[i+j+1]

    if sumB > sumA:
      count += 1
  return count


print(windowIncrease(lines,1))