import re
import numpy as np
p1 = 0
with open('day4_input.txt', 'r') as file:
  lines = file.readlines()
delta = np.ones(len(lines))
for i in range(len(lines)):
  parts = re.sub(re.compile(fr'Card\s*{i+1}:\s*'), '', lines[i]).split('|')
  intersect = np.intersect1d(np.fromstring(parts[0], sep=' '), np.fromstring(parts[1], sep=' ')).size
  p1 += 2**(intersect - 1) if intersect != 0 else 0
  delta[i+1:i+intersect+1] += delta[i]
print(p1, np.sum(delta))