import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N,M,R = map(int, input().split())
graph = [[] for _ in range(N+1)] # range 돌면서 미리 graph를 선언해줘야함. 

#R에서 시작.
#input
for i in range(M):
    inputcord = list(map(int, input().split()))
    graph[inputcord[0]].append(inputcord[1])
    graph[inputcord[1]].append(inputcord[0]) #undirected라서 양쪽다 연결해줘야함
    
vorder=[0]*(N+1) #order 입력할 리스트
vnumber = 0 #순서값

def dfs(graph,R,visited):
    global vnumber
    visited[R] = True #방문처리
    vnumber += 1
    vorder[R] = vnumber
    for e in sorted(graph[R]): #오름차순으로 방문
        if visited[e] == False:
            dfs(graph,e,visited)
            
visited = [False]*(N+1) #노드개수만큼 
dfs(graph,R,visited)

# i번째 줄에는 정점 i의 방문 순서를 출력
for j in range(1,N+1):
    print(vorder[j])