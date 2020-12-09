with open('input.txt') as f:
    content = f.readlines()

temp = ''
count = 0
for line in content:
    if line != '\n':
        line = line.strip()
        for char in line:
            if char not in temp:
                temp += char
    else:
        count+=len(temp)
        temp = ''


print(count+len(temp))