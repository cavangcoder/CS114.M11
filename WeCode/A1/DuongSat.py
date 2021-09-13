k, t = map(int, input().split())
if ((t//k)&1): 
    print(k - (t%k))
else:
    print(t%k)