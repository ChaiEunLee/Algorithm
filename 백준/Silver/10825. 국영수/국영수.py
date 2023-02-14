N = int(input())

inputlist = []

for i in range(N):
    name, kor, eng, math = map(str, input().split())
    inputlist.append([name, int(kor), int(eng), int(math)])
    
sortlist = sorted(inputlist, key = lambda x: (-x[1],x[2],-x[3],x[0]))

for i in range(N):
    print(sortlist[i][0])