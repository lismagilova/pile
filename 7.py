n = str(input())
mx = 0
for num in range(len(n)):
    if int(n[num]) > mx:
        mx = int(n[num])
print(mx)