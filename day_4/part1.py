with open('input.txt') as f:
    content = f.readlines()

a = dict()
lookup = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
count = 0
out = 0
for line in content:
    if line != '\n':
        fields = line.split()
        for item in fields:
            key = item.split(':')[0]
            value = item.split(':')[1]
            a[key] = value

            if key in lookup:
                count += 1
    else:
        if count == len(lookup):
            out+=1
        count = 0
        a = dict()
else:
    if count == len(lookup):
        out+=1

print(out)