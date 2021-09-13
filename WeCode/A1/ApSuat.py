from decimal import *

n = float(input()) * 0.453592 / (2.54 ** 2)

getcontext().prec = 6
print(Decimal(n).normalize())