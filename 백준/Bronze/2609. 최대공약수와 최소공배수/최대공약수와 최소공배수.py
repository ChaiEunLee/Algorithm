n,m = map(int, input().split())

a=2

res_min = 1
res_max = 1

while n>=a and m>=a:
    if n%a==0 and m%a==0:
        n = n/a
        m = m/a
        res_min = res_min*a
    else:
        a += 1
        
res_max = int(res_min*n*m)

print(res_min)
print(res_max)