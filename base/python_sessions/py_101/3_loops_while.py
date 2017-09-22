# Program to add natural nos
# unto n i.e sum = 1+2+3+..n

n = 10
total, cntr = 0, 1

while cntr <= n:
    total += cntr
    cntr += 1

print('Total: %d' % total)
