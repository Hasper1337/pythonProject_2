def m(n):
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0 and x != n // x:
            return x + n // x
    return 0

k = 0
for i in range(452021, 1000000):
    if m(i) % 7 == 3:
        print(i, "|", m(i), "<- sum del")
        k += 1
    if k == 5:
        break