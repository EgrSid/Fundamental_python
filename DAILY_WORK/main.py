def f(x):
    res = ''
    while x > 0:
        res = str(x % 6) + res
        x //= 6
    return res


for i in range(1, 1000):
    num = f(i)
    if i % 3 == 0:
        num = num + num[:2]
    else:
        num = num + f(i % 3 * 10)

    res = int(num, 6)
    if res > 680:
        print(res)
        break
