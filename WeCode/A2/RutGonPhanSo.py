def gcd(a, b) :
    while b > 0 :
        a,b = b, a % b
    return a

testcase = int(input())
for i in range(testcase) :
    a , b = map(int, input().split())
    r = gcd(a,b)
    print(a//r, b//r if b//r>1 else "")
