import sys

inp = list(map(int, sys.stdin.readline().split()))
users = set()

while inp[0] > 0 :
    if inp[0] == 1 :
        users.add(inp[1])
    else : 
        sys.stdout.write("1\n" if inp[1] in users else "0\n")
    inp = list(map(int, sys.stdin.readline().split()))