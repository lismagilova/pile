n = int(input())
mas = list(str(n))
new = []
for i in range(len(mas)):
    if int(mas[i]) % 2 != 0:
        new.append(mas[i])
print("".join(new))