with open('input.txt') as f:
    content = f.readlines()

a = list()
for line in content:
    a.append(line.strip())

i = 0
j = 0
count = 0
while i < len(a):
    if a[i][j] == '#':
        count+=1
    i+=1
    j+=3
    if j >= len(a[0]):
        j -= len(a[0])

print(count)