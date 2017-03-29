
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

N=0
M=0
steps = 0
res = []
count = 1
with open('result.txt') as f:
    N, M, steps = [int(x) for x in next(f).split()] # read first line
    ct = 1
    temp = []
    for line in f: # read rest of lines
        temp.append([int(x) for x in line.split()])
        if ct % M == 0:
            res.append(temp)
            temp=[]
        ct+=1

new_res = []
for x in res:
  temp1 = []
  for y in x:
    temp2 = []
    for z in y:
      if z == 1:
        temp2.append(255)
      else:
        temp2.append(0)
    temp1.append(temp2)
  new_res.append(temp1)
res = new_res

grid = np.array(res[0])

def update(data):
  global grid
  global count
  global steps
  newGrid = grid.copy()
  newGrid=np.array(res[count%steps])
  count+=1
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]

fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=1000,
                              save_count=50)
plt.show()
