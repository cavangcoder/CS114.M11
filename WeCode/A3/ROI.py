import sys

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
x1, y1, x2, y2 = map(int, input().split())

ans = [[0]*m for i in range(n)]
for i in range(x1,x2+1) :
    for j in range(y1,y2+1):
        ans[i][j] = a[i][j]
s = ""
for i in range(n) :
    s += " ".join(map(str,ans[i])) + "\n"
sys.stdout.write(s)
