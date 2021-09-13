x, y = map(int, input().split())
dog     = (y - x - x) >> 1
chicken = x - dog 
print(chicken, dog)