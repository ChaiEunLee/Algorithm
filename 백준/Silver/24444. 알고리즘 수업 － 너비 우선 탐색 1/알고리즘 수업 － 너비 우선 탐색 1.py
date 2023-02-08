#RecursionError 때문에
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

from collections import deque

N,M,R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
vorder = [0]*(N+1)
vnumber = 1

def bfs(graph, visited, R):
    global vnumber
    queue = deque([R])
    visited[R] = True
    vorder[R] = vnumber
    while queue:
        v = queue.popleft()
        for q in sorted(graph[v]):
            if not visited[q]:
                queue.append(q)
                visited[q] = True
                vnumber += 1
                vorder[q] = vnumber
                
visited = [False]*(N+1)
bfs(graph, visited, R)

for j in range(1,N+1):
    print(vorder[j])