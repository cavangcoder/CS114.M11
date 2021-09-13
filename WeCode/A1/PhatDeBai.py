n = int(input())
k = int(input())
p = int(input())
q = int(input())

id_Alice = 2 * (p - 1) + q

if (id_Alice - k > 0) :
    id_Bob = id_Alice - k
else :
    id_Bob = id_Alice + k

if id_Bob > n or id_Bob < 1:
    print(-1)
else:
    print((id_Bob + 1) // 2, 2 - (id_Bob % 2))

