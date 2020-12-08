with open('input.txt') as f:
    content = f.readlines()

a = dict()
for line in content:
    line = int(line)
    if a.get(2020-line) is not None:
        print((2020-line)*line)
        break
    a[line] = 1
