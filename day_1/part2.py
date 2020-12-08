with open('input.txt') as f:
    content = f.readlines()
a = list()
for line in content:
    line = int(line)
    for number in a:
        if number + line < 2020:
            for number2 in a :
                if number != number2 and number + number2 + line == 2020:
                    print(number*number2*line)

    a.append(line)