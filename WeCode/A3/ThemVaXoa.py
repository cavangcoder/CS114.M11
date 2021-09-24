import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

arr = list()
inp = list(map(int, input().split()))

while inp[0] < 6:
    if inp[0] == 0: arr.insert(0, inp[1])
    elif inp[0] == 1: arr.append(inp[1])
    elif inp[0] == 2:
        try: arr.insert(arr.index(inp[1]) + 1, inp[2])
        except: arr.insert(0, inp[2])
    elif inp[0] == 3:
        try: arr.remove(inp[1])
        except: pass;

    elif inp[0] == 4: arr = list(filter(lambda e: e != inp[1], arr))
    elif inp[0] == 5: 
        if len(arr) != 0:
            arr.pop(0)
    inp = list(map(int, input().split()))

print(' '.join(map(str, arr)) if len(arr) else 'blank')