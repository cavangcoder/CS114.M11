from decimal import *
getcontext().prec = 6

f = float(input())
c = 5/9 * (f - 32)
k = 5/9 * (f - 32) + 273.15

print(Decimal(c).normalize(), Decimal(k).normalize())