import time
import sys
start_time = time.time()

directions = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}
tilelist = {
    "-": [["R", "L"], ["R", "L"]],
    "|": [["U", "D"], ["U", "D"]],
    "7": [["R", "U"], ["D", "L"]],
    "J": [["R", "D"], ["U", "L"]],
    "L": [["D", "L"], ["R", "U"]],
    "F": [["U", "L"], ["R", "D"]]
}

def mov(c, dir):
  tile = tilelist.get(array[c[0]][c[1]])
  if dir in tile[0]:
    dir_index = tile[0].index(dir)
    c = [sum(x) for x in zip(c, directions[tile[1][dir_index]], strict=True)]
    return (c, tile[1][dir_index])
  else:
    print(f"break: {c}, {dir}")

def recursive(c1, d1, c2, d2, i):
  c1, d1 = mov(c1, d1)
  c2, d2 = mov(c2, d2)
  return (c1, c2, i + 1) if c1 == c2 else recursive(c1, d1, c2, d2, i + 1)

array = []
s_pos = [0, 0]
with open("day10_input.txt", "r") as f:
  for i, line in enumerate(f.readlines()):
    if "S" in line:
      s_pos = [i, line.index("S")]
    array.append(list(line.strip()))
sys.setrecursionlimit(10000)
cc1, cc2 = None, None
for dir, offset in directions.items():
  c = [sum(z) for z in zip(s_pos, offset, strict=True)]
  if 0 <= c[0] < len(array) and 0 <= c[1] < len(array[0]):
    tile = tilelist.get(array[c[0]][c[1]])
    if tile and any(mov(c, pos)[0] == s_pos for pos in tile[0]):
      cc1, cc2 = ([c, dir], cc2) if cc1 is None else (cc1, [c, dir])
c1, c2, i = recursive(*cc1, *cc2, 1)
print(f'{i} {(time.time()-start_time)}s')
