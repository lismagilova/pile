a = str(input())
b = []
c = ''
for i in range(len(a)):
    b.append(a[i])
b.reverse()
for k in range(len(b)):
    c = c + b[k]
print(c)