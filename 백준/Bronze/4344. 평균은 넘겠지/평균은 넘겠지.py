
C = int(input())
for i in range(C):
    A = list(map(int, input().split()))
    class_mean = sum(A[1:])/A[0]
    cnt = 0
    for i in range(1,len(A)):
        if A[i] > class_mean:
            cnt+=1
    prop = cnt/A[0]*100
    print('{:.3f}'.format(prop)+"%")