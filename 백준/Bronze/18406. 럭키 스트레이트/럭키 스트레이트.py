N = int(input())

strN = str(N)
front = strN[0:int(len(str(N))/2)]
back = strN[int(len(str(N))/2):len(str(N))]

frontsum = 0
backsum = 0
for i in range(len(front)):
    frontsum += int(front[i])
for j in range(len(back)):
    backsum += int(back[j])
    
if frontsum == backsum:
    print("LUCKY")
else:
    print("READY")