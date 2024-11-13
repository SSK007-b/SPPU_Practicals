n = int(input("Enter the Number of Objects "))
m = int(input("Enter the Capacity "))

p = [0]
w = [0]
ans = []

for i in range(n):
    weight = int(input("Enter the Weight "))
    w.append(weight)
    profit = int(input("Enter the Profit "))
    p.append(profit)
    ans.append(0)

t = []
for i in range(n+1):
    t.append([])
    for j in range(m+1):
        t[i].append(0)

for i in range(n+1):
    for j in range(m+1):
        a = w[i]
        if j >= a:
            t[i][j] = max(t[i-1][j], p[i] + t[i-1][j-w[i]])
        else:
            t[i][j] = t[i-1][j]

for i in range(m+1):
    print(i, end='\t')
print()

for i in t:
    for j in i:
        print(j, end='\t')
    print()

print("The Maximum Profit is ", t[-1][-1])

res = t[-1][-1]
wgt = m

for i in range(n, 0, -1):
    if res <= 0:
        break
    if res == t[i-1][wgt]:
        continue
    else:
        ans[i-1] = 1
        res -= p[i]
        wgt -= w[i]

print("The Selected Objects are ", ans)