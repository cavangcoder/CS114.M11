m = n = int(input())
sqrt_n = int (n ** 0.5)

ans = 1
for i in range(2,sqrt_n+1) :
    div_num = 1
    while n % i == 0 :
        n //= i
        div_num *= i
    if div_num == 1 : continue
    ans *= ((div_num * i - 1) // (i - 1))

if n > 1 :
    ans *= (n * n - 1) // (n-1)

ans = max(1, ans - m)
print(ans)