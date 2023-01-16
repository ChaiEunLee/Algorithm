N = int(input())
numlist = []
for i in range(N):
    numlist.append(int(input()))

numlist_sorted = sorted(numlist)
for i in range(N):
    print(numlist_sorted[i])