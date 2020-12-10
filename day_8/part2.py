#kind of greedy approach
#the line that causes the infinite loop has to be before where the first repeat of instruction is.
#loop over all jmps and nops before the first repeat of instruction and reverse them to see
#if it we can loop to EOF

import re
with open('test.txt') as f:
    content = f.readlines()

seen = set()
seen_jmp_or_nop = set()
count = 0
i = 0
reverse_dict = {"jmp": "nop", "nop": "jmp"}
while i < len(content):
    if i+1 in seen:
        break
    seen.add(i+1)
    line = content[i]
    action = line.split(" ")[0]
    num = int(line.split(" ")[1])
    if action == "acc":
        count += num
        i += 1
    elif action == "jmp":
        seen_jmp_or_nop.add(i+1)
        i = i + num
    else:
        seen_jmp_or_nop.add(i+1)
        i += 1

for x in seen_jmp_or_nop:
    i = 0
    seen = set()
    count = 0
    while i < len(content):
        if i+1 in seen:
            break
        seen.add(i+1)
        line = content[i]
        action = line.split(" ")[0]
        num = int(line.split(" ")[1])
        if i+1 == x:
            action = reverse_dict[action]
        if action == "acc":
            count += num
            i += 1
        elif action == "jmp":
            i = i + num
        else:
            i += 1
    else:
        break
print(count)