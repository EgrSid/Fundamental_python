a = list(map(int, input().split('.')))  # вася res1
b = [29, 2, a[-1]]  # петя res2
c = list(map(int, input().split('.')))  # сейчас дата

res2 = (c[2] - a[2]) // 4 + 1

if a == b:
    res1 = res2
else:
    if a[1] < c[1]:
        res1 = c[2] - a[2] + 1
    else:
        res1 = c[2] - a[2]
print(res2, res1)


