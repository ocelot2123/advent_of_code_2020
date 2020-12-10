with open('input.txt') as f:
    content = f.readlines()

#err = 127 #test
err = 675280050
a = []
for line in content:
    a.append(int(line))

start = 0
end = 0
out = a[0]

while out != err:
    if out < err:
        end += 1
        out += a[end]
    else:
        out -= a[start]
        start += 1

res_list = sorted(a[start:end+1])
print(res_list[0] + res_list[-1])