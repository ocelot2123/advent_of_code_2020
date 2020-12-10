with open('input.txt') as f:
    content = f.readlines()

a = []
count_1 = 0
count_3 = 0
for line in content:
    a.append(int(line))

a = sorted(a)
a.append(a[-1]+3)

pre = 0
for num in a:
    if num - pre == 1:
        count_1+=1
    elif num - pre == 3:
        count_3+=1
    pre = num

print(count_1 * count_3)