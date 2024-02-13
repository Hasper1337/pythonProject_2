x = 16**18 * 4**10 - 46 - 16
s = ""
while x != 0:
    s += str(x % 3)
    x /= 3
print(s.count("3"))