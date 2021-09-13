a = int(input())
b = int(input())
c = int(input())

a, b, c = sorted([a,b,c])

if c >= a + b:
    print('Khong phai tam giac')
    exit()

tri = "thuong"
if   a == b and b == c      : tri = "deu"
elif a == b or  b == c      : tri = "can"
elif a * a + b * b == c * c : tri = "vuong"

p    = (a + b + c) / 2
area = round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)

if abs(area - int(area)) < 0.001 : area = int(area)
print(f"Tam giac {tri}, dien tich = {area}")
 


