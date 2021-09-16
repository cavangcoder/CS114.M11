str = input()
n   = int(str)
pow = len(str)
sum = 0

for v in str :
    sum += int(v) ** pow

if sum == n :
    print("True")
else :
    print("False")
