import collections
import heapq

def dijkstra(n, graph):
    q = []
    heapq.heappush(q, [0, 0])

    dist = collections.defaultdict(int)

    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                heapq.heappush(q, [time + w, v])
    
    for i in range(n):
        if i in dist:
            print(dist[i])
        else:
            print('INF')

n = 5
graph = [[[1, 1], [3, 2]]
        ,[[0, 1], [2, 3]]
        ,[[0, 2]]
        ,[[1, 2], [2, 1]]
        ,[[3, 2]]
        ]
dijkstra(n, graph)