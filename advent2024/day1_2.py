file_name = 'day1_input.txt'

column_a = []
column_b = []

with open(file_name, 'r') as file:
    for line in file:
        a, b = map(int, line.split())
        column_a.append(a)
        column_b.append(b)


column_a.sort()
column_b.sort()
b_dict = dict();
c = 0

# turn column b into dictionary
for i in range(len(column_b)):
    if column_b[i] in column_a:
        b_dict[column_b[i]] = b_dict.get(column_b[i], 0) + column_b[i]


print(sum(b_dict.values()))