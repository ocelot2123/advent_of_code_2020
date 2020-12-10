with open('input.txt') as f:
    content = f.readlines()

a = []

for line in content:
    a.append(int(line))

a.append(0)
a = sorted(a)

dp = {}

for i in a:
    if i == 0:
        dp[i] = 1
        continue
    out = 0
    for j in range(i-3, i):
        if j in a:
            out += dp[j]
    dp[i] = out

print(dp.get(a[-1]))
