first = str(input())
mas = []
ans = 0
for num in range(len(first)):
    mas.append(int(first[num]))
for quan in range(len(mas)):
    if quan % 2 == 0:
        ans = ans + mas[quan]
    else:
        ans = ans - mas[quan]
print(ans)
