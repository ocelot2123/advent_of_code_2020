with open('input.txt') as f:
    content = f.readlines()

temp = set()
count = 0
flag = True
for line in content:
    if line != '\n':
        line = line.strip()
        a = set()
        for char in line:
            a.add(char)
        if flag:
            flag = False
            temp = a
        else:
            temp = temp.intersection(a)
    else:
        count+=len(temp)
        temp = set()
        flag = True


print(count+len(temp))