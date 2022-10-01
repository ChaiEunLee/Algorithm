#selection sort
sortlist = []
N = int(input())
for num in range(N):
    n = int(input())
    sortlist.append(n)
    
for i in range(len(sortlist)):
    minval = sortlist[i]
    for j in range(i,len(sortlist)):
        if sortlist[j] < minval:
            minval = sortlist[j]
            minidx = j
    if sortlist[i] > minval:
        sortlist[i], sortlist[minidx] = sortlist[minidx], sortlist[i]
    print(sortlist[i])