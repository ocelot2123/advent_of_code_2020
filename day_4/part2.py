
import re

with open("input.txt") as f:
    content = f.readlines()

a = dict()
lookup = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
regex_lookup = {
    "byr": "^19[2-9][0-9]|200[0-2]$",
    "iyr": "^201[0-9]|2020$",
    "eyr": "^202[0-9]|2030$",
    "hgt": "^((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)$",
    "hcl": "^#[0-9a-f]{6}$",
    "ecl": "^(amb|blu|brn|gry|grn|hzl|oth)$",
    "pid": "^[0-9]{9}$",
}

count = 0
out = 0
for line in content:
    if line != "\n":
        fields = line.split()
        for item in fields:
            key = item.split(":")[0]
            value = item.split(":")[1]
            a[key] = value
            if key not in lookup:
                continue

            if re.compile(regex_lookup[key]).match(value):
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