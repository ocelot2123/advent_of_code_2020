def binary_search(low, high, x): 
    mid = (high + low) // 2
    if not x:
        return mid

    elif x[0] == 'F' or x[0] == 'L': 
        return binary_search(low, mid, x[1:])

    else: 
        return binary_search(mid + 1, high, x[1:])

with open('input.txt') as f:
    content = f.readlines()

maxi = 0
for line in content:
    if (cur := binary_search(0,127,line[:7]) * 8 + binary_search(0,7,line[7:])) > maxi:
        maxi = cur

print(maxi)