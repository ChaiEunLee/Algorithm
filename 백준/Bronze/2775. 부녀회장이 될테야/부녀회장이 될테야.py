T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    top = 1
    bottom = 1
    denom = k+n
    numer = n

    for i in range(n-1):
        top *= denom
        denom -= 1
    for i in range(n-1):
        bottom *= (numer-1)
        numer -= 1

    print(int(top/bottom))