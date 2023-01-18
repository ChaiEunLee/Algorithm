N = int(input())
nlist = [0]*N
nlist = list(map(int, input().split()))
nlist.sort()
print(nlist[0]*nlist[len(nlist)-1])