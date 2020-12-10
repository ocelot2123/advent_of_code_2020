with open('input.txt') as f:
    content = f.readlines()

a = []
for line in content:
    a.append(int(line))
preamble = 25
bad = 0
for idx in range(preamble, len(a)):
    val = a[idx]
    for i in range(idx-preamble, idx):
        indices = [b for b in range(idx-preamble, idx) if a[b] == (val - a[i])]
        if indices:
            break
    else:
        bad = val
        break

print(bad)