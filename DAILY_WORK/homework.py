from itertools import product


def f(x):
    res = 0
    for i, el in enumerate(x[:-2]):
        if x.count(el) == 3:
            if x[i + 1] == el and x[i + 2] == el and len(set(x)) == 3:
                res += 1
    return True if res == 1 else False


word = '01234567'
k = 0
for i in product(word, repeat=5):
    s = ''.join(i)
    print(s, f(s))
    if s[0] != '0':
        if f(s):
            k += 1
print(k)
