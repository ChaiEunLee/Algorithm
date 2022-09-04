H, M = map(int, input().split())

if int(M) - 45 <0:
    M = int(M)+15
    if int(H) - 1 < 0:
        H = int(H)+23
    else:
        H = int(H)-1
else:
    M = int(M) - 45
    H = int(H)
    
print(H, M)