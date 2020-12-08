with open('input.txt') as f:
    content = f.readlines()

a = list()
for line in content:
    a.append(line.strip())

listi = [1,1,1,1,2]
listj = [1,3,5,7,1]

out = 0

for idx, val in enumerate(listi):
    count = 0
    i = 0
    j = 0
    while i < len(a):
        if a[i][j] == '#':
            count+=1
        i+=val
        j+=listj[idx]
        if j >= len(a[0]):
            j -= len(a[0])

    if out == 0:
        out += count
    else:
        out *= count

print(out)