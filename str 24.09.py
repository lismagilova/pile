a = str(input())
b = str(input())
e = list(a)
f = list(b)
e.sort()
f.sort()
if e == f:
    print(True)
else:
    print(False)