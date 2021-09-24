import sys

n, m = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())

a = []
for i in range(n) :
    for v in map(int, sys.stdin.readline().split()) :
        a.append(v)

if n * m != p * q :
    p, q = n, m

for i in range(p) :
    sys.stdout.write(" ".join(map(str,a[i*q : i*q+q])) + "\n")