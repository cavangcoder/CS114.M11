testcase = int(input())
for i in range(testcase) :
    n = int (input())
    total = sum(map(int, input().split()))
    print(total // n + (total % n > 0))
