n = int(input())
k = 0
step = 0
sum = 0
while step < n:
    k = k + 10 ** step
    step = step + 1
    sum = sum + k
print(sum)

# n = int(input())
# step = 1
# k = 1
# sum = 0
# while step <= n:
#     sum = sum + k
#     k = k + 10 ** step
#     step = step + 1
# print(sum)
