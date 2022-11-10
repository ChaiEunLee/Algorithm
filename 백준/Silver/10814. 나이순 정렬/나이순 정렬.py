import sys

#N = int(input())
N = int(sys.stdin.readline())
userlist = []

for i in range(N):
#    age, name = input().split()
    age, name = sys.stdin.readline().split()
    userlist.append([int(age),name])
    
userlist = sorted(userlist, key = lambda x:(x[0]))

for i in range(N):
    print(userlist[i][0], userlist[i][1])