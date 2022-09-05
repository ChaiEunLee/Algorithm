H, M = map(int, input().split())
T = input()

H = int(H)
M = int(M) + int(T)

total = 60*H + M
H = total//60
M = total%60

if H >= 24:
    H = H - 24

print(H, M)