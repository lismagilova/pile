n = int(input())
count = 0
check = False

for i in range(n):
    a = int(input())
    c = 0
    mas = list(str(a))

    if int(mas[0]) % 2 != 0:
        for i in range(len(mas)):
            if int(mas[i]) % 2 != 0:
                c = c + 1

    else:
        for i in range(len(mas)):
            if int(mas[i]) % 2 == 0:
                c = c + 1

    if len(mas) == c == 3 or len(mas) == c == 5:
        count = count + 1

if count == 2:
    check = True
print(check)