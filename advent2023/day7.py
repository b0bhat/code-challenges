# Solver for https://adventofcode.com/2023/day/7
import time

start_time = time.time()
replacement = {'A': 'A', 'K': 'B', 'Q': 'C', 'T': 'E', '9': 'F', '8': 'G', '7': 'H', '6': 'I', '5': 'K', '4': 'L', '3': 'M', '2': 'N', 'J': 'Z'}

def dictify(item):
  count = {i: item.count(i) for i in set(item)}
  if 'Z' in count:
    if count['Z'] < 5: del count['Z']
    maxnum = max(count, key=count.get)
    count[maxnum] += count['Z']
  return count

def sort_in_tiers(sorted_tier, max_freq_of_larger_type=0):
  sorted_tier.sort(key=lambda x: x[0])
  if max_freq_of_larger_type != 0:
    larger_type, smaller_type = [], []
    for item in sorted_tier:
      (smaller_type, larger_type
       )[max(item[2].values()) == max_freq_of_larger_type].append(item)
    sorted_tier = larger_type + smaller_type
  return sorted_tier

sorted = [[], [], [], [], []]
inty = 0
with open("day7_input.txt", "r") as f:
  for line in f.read().split('\n'):
    hand, bid = line.split(' ')
    hand_alpha = ''.join(replacement[number[0]] for number in hand)
    hand_dict = dictify(hand_alpha)
    sorted[len(hand_dict) - 1].append([hand_alpha, int(bid), hand_dict])

all = []
for i in range(5):
  max_freq = 4 if i == 1 else (3 if i == 2 else 0)
  all += sort_in_tiers(sorted[i], max_freq)
add = sum((hand[1] * (len(all) - i)) for i, hand in enumerate(all))
print(f'{add} : {(time.time()-start_time)}s')
