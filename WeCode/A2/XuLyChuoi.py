string = input().lower()
na = ['a','o','y','e','u','i']

for v in na :
    string = string.replace(v,'')

print('.' + '.'.join(string))