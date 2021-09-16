n, m, k  = map(int, input().split())
print( (n//k + (n%k>0)) * (m//k + (m%k>0)))