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
c = 0

for i in range(len(column_a)):
    c += abs(column_a[i] - column_b[i])
    
print(c)