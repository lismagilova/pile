indexs = [1, 2, 3, 4, 5]
a2 = [2, 3, 5, 1, 4]
b2 = [2, 1, 5, 3, 4]
c2 = []
for i in range(len(a2)):
    for k in range(len(indexs)):
        if a2[i] == indexs[k]:
            c2.insert(i, b2[k])
a2 = c2
print(indexs, a2)
