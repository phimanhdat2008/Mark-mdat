def gt(d):
    if d == 1:
        return 1
    return d * gt(d-1)

def mau(k):
    result = 1
    for i in range(2, k+1):
        result *= gt(i)
    return result

def lt(v):
    t = 0
    for j in range(2, v+1):
        if j % 2 == 0:
            t += (-1) ** j
        if j % 2 != 0:
            t += (1) ** j
    return t

a = input("nhập lần lượt X và N : ")
b = str(a).split(" ")
x, n = b[0], b[1]
e = int(n)
c = int(x)

s = 1
for i in range(1, c+1):
    s *= (-1)**i + 1

print(s)
