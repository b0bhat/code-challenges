import time

start_time = time.time()

array = []
s_pos = [0, 0]
with open("oof.txt", "r") as f:
  for i, line in enumerate(f.readlines()):
    if "S" in line:
      s_pos = [i, line.index("S")]
    array.append(list(line.strip()))

directions = {
  "R" : [0, 1],
  "L" : [0, -1],
  "U" : [-1, 0],
  "D" : [1, 0]
}

tilelist = {
    "-": ["R", [0, +1], "L", [0, -1], "R", "L"],
    "|": ["U", [-1, 0], "D", [+1, 0], "U", "D"],
    "7": ["R", [+1, 0], "U", [0, -1], "D", "L"],
    "J": ["R", [-1, 0], "D", [0, -1], "U", "L"],
    "L": ["D", [0, +1], "L", [-1, 0], "R", "U"],
    "F": ["U", [0, +1], "L", [+1, 0], "R", "D"],
}

cc1 = None
cc2 = None


def mov(c, dir):
  obj = tilelist[array[c[0]][c[1]]]
  if dir == obj[0]:
    c = [sum(x) for x in zip(c, obj[1], strict=True)]
    return (c, obj[4])
  elif dir == obj[2]:
    c = [sum(x) for x in zip(c, obj[3], strict=True)]
    return (c, obj[5])
  else:
    print("break")
    return


def start(x, y, dir):
  global cc1, cc2
  tile = tilelist.get(array[x][y])
  if tile is None:
    return
  if (0 <= x < len(array) and 0 <= y < len(array[0])
      and ((mov([x, y], tile[0])[0] == s_pos) or
           (mov([x, y], tile[2])[0] == s_pos))):
    if cc1 is None:
      cc1 = [[x, y], dir]
    else:
      cc2 = [[x, y], dir]


start(s_pos[0] - 1, s_pos[1], "U")
start(s_pos[0] + 1, s_pos[1], "D")
start(s_pos[0], s_pos[1] - 1, "L")
start(s_pos[0], s_pos[1] + 1, "R")

i = 1
c1, d1 = mov(cc1[0], cc1[1])
c2, d2 = mov(cc2[0], cc2[1])
while True:
  c1, d1 = mov(c1, d1)
  c2, d2 = mov(c2, d2)
  i += 1
  if c1 == c2 or i > 10000:
    print(f'{c1} {c2} {i+1}')
    break

print(f'{(time.time()-start_time)}s')
