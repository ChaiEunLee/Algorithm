#이렇게 풀었더니 런타임 에러.
import sys

#N = int(input())
N = int(sys.stdin.readline())
sortlist = [0]*10001 #입력가능한 수는 10,000 이하임. 그래서 굳이 10,000,000 array를 안 만들어도 됨.

for i in range(N):
#    num = int(input())
#    num = int(sys.stdin.readline())
    sortlist[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    if (sortlist[i] != 0): #if (sortlist[i] > 0): 이렇게 해도 안되고 
        for j in range(sortlist[i]):
            print(i)
#        print((str(i)+'\n')*sortlist[j],end='')