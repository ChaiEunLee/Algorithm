X = input()
N = input()
Xpred = 0

for i in range(0, int(N)):
    a, b = map(int, input().split())
    Xpred += a*b

if Xpred == int(X):
    print("Yes")
else:
    print("No")