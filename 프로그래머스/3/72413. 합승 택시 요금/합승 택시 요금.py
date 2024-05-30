import heapq
INF = 1e8

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        u,v,w = fare[0], fare[1], fare[2]
        graph[u].append((v,w))
        graph[v].append((u,w))
        
    def dijkstra(s, dst): #start -> destination
        distance = [INF]*(n+1)
        q = []
        heapq.heappush(q,(0,s))
        distance[s] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                v,w = i[0], i[1]
                if dist+w < distance[v]:
                    distance[v] = dist+w
                    heapq.heappush(q,(dist+w,v))
        return distance[dst]
    
    cost = dijkstra(s,a)+dijkstra(s,b)
    for i in range(1,n+1):
            if i!=s:
                cost = min(cost, dijkstra(s,i)+dijkstra(i,a)+dijkstra(i,b))
    return cost
        
        
        
    answer = 0
    return answer