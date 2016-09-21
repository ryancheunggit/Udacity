s = 1000000000

for i in range(1000000):
    s += 0.000001

print round(s-1000000000,3)