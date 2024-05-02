# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
#import sys
#sys.stdin = open("input.txt", "r")

#T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(10):
    test,N = map(int,input().split())
    #N input road number
    road = list(map(int,input().split()))
    roaddict = {}
    for i in range(0,N*2,2):
        #print(road[i], road[i+1])
        a,b = road[i], road[i + 1]
        if a in roaddict:
            roaddict[a].append(b)
        else:
            roaddict[a] = [b]

    # 99에 도착하면 return 1
    # DFS로 가다가 이미 지나간대로 돌아오면 return
    # 갈 곳이 없으면 return
    # array 안 만들고 dfs로.
    #print(roaddict)
    
    def dfs(number, visited):
        global answer
        #print(number, visited)
        # 99에 도착하면 return 1
        if number == 99:
            answer = 1
            return 1

        # DFS로 가다가 이미 지나간대로 돌아오면 return
        if visited[number]:
            #print("already visited")
            return
        # 갈 곳이 없으면 return
        if number not in roaddict:
            #print('no further road')
            return

        visited[number] = True
        for k in roaddict[number]:
            newvisited = visited.copy()
            dfs(k, newvisited)
            if answer == 1:
                return
            
    visited = [False]*100
    answer = 0
    dfs(0, visited)
    #print(answer)
    print('#{} {}'.format(test, answer))
