N,K = map(int,input().split())
A = list(map(int,input().split()))

robot = [0]*len(A) # robot location
#robot[0] = 1
#A[0] -= 1
step = 0
cnt = A.count(0)
# 2: 로봇 한칸 이동&컨베이어 이동 & 새로운 로봇 내구도 확인하고 올리기  

while True:
    if cnt >= K:
        print(step)
        break
    # 컨베이어 이동
    step += 1
    A = [A[-1]]+A[:-1]
    robot = [robot[-1]]+robot[:-1]
    #robot[(len(robot)//2)-1]= 0 #하차
    #print(A,robot)
    # 로봇 한칸 이동
    for i in range((len(robot)//2)-1,0,-1): #0에는 무조건 없을거고, 
        if robot[i] == 1:
            if i==(len(robot)//2)-1: #하차 지점
                robot[i] = 0 # 내리기
            elif A[i+1]>0 and robot[i+1] == 0:
                robot[i], robot[i+1] = 0,1
                A[i+1] -= 1
                if A[i+1]==0:
                    cnt += 1
    robot[(len(robot)//2)-1]= 0
    # 새로운 로봇 올리기
    #print(A,robot)
    if A[0] > 0 and robot[0]==0:
        A[0] -= 1
        robot[0] = 1
        if A[0] == 0:
            cnt += 1