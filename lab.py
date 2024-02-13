from itertools import *

sl = "НАСТЯ"
count = 0
for i in product("НАСТЯ", repeat=6):
    if i.count("А")>1:
        continue
    if i.count("Я") > 1:
        continue
    count += 1
print(count) #6075