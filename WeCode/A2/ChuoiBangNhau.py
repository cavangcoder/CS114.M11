for i in range(int(input())) :
    print('YES' if len(set(input()).intersection(set(input()))) > 0 else 'NO')