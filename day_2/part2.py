import re

with open('input.txt') as f:
    content = f.readlines()

count = 0
for line in content:
    line = line.strip()
    inp = re.split('-| |: ', line)
    if (inp[3][int(inp[0])-1] == inp[2] or inp[3][int(inp[1])-1] == inp[2]) and inp[3][int(inp[0])-1]!=inp[3][int(inp[1])-1]:
        count+=1

print(count)