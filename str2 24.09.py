a = list(map(int, input().split()))
c = int(input())
b = 0
a.reverse()
for i in range((len(a) - 1)):
    b = b + int(a[i] * (10**i))


print(a)