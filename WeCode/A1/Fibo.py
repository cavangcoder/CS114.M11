n = int(input())
if not n in range(1,31) :
    print("So", n, "khong nam trong khoang [1,30].")
else :
    fibo_1 = fibo_2 = 1
    for i in range(3, n + 1) :
        fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2

    print(fibo_2)