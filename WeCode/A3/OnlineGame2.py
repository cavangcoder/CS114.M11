import sys

inp = list(map(int, sys.stdin.readline().split()))
users = set()

while inp[0] > 0 :
    if inp[0] == 1 :
        if not inp[1] in users :
            users.add(inp[1])
    elif inp[0] == 2 : 
        sys.stdout.write("1\n" if inp[1] in users else "0\n")
    elif inp[1] in users :
        users.remove(inp[1])

    inp = list(map(int, sys.stdin.readline().split()))