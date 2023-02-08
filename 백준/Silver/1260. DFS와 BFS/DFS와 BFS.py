N,M,V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
#DFS
def DFS(graph, visited, V):
    visited[V] = True
    print(V, end=' ')
    for v in sorted(graph[V]):
        if visited[v] == False:
            DFS(graph, visited, v)    

visited = [False]*(N+1)
DFS(graph, visited, V)
print()

from collections import deque
def BFS(graph, visited, V):
    queue = deque([V])
    visited[V] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
visited = [False]*(N+1)
BFS(graph, visited, V)