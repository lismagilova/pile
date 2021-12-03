dnk = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
n = set()
for i in range(len(dnk) - 20):
    for j in range(i + 10, len(dnk) - 10):
        count = 0
        m = ''
        for a in range(10):
            if dnk[i + a] == dnk[j + a]:
                count = count + 1
                m = m + dnk[i + a]
        if count == 10 and m not in n:
            n.add(m)
print(n)