import re

with open('input.txt') as f:
    content = f.readlines()

seen = set()
count = 0
i = 0
while i < len(content):
    if i+1 in seen:
        break
    seen.add(i+1)
    line = content[i]
    action = line.split(" ")[0]
    num = line.split(" ")[1]
    num = int(num)
    if action == "acc":
        count += num
        i += 1
    elif action == "jmp":
        i = i + num
    else:
        i += 1

print(count)