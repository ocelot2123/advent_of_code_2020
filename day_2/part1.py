import re

with open('input.txt') as f:
    content = f.readlines()

count = 0
for line in content:
    line = line.strip()
    inp = re.split('-| |: ', line)
    if inp[3].count(inp[2]) >= int(inp[0]) and inp[3].count(inp[2]) <= int(inp[1]):
        count+=1

print(count)