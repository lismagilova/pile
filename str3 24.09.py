a = list(map(int, input().split()))
c = int(input())
b = 0
e = []
a.reverse()
for i in range(len(a)):
    b = b + (int(a[i]) * int(10**(i)))
b = b + c
d = str(b)
for k in range(len(d)):
    e.append(d[k])
print(e)