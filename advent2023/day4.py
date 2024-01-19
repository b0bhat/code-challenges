import re
m = 0
with open('day4_input.txt', 'r') as file:
    for i, line in enumerate(file):
      parts = re.sub(re.compile(fr'Card\s*{i+1}:\s*'), '', line).split('|')
      y = len(list(set(map(int, parts[0].split())).intersection(set(map(int, parts[1].split())))))
      m += 2**(y-1) if y != 0 else 0
print(m)