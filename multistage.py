import collections as ct

INF=999999999999

def shortest_dist(graph, final_node):
    n=final_node+1
    dist=[0]*n
    dist[n-1]=0
    for i in range(n-2, -1, -1):
        dist[i] = INF
        for j in range(n):
            if graph[i][j]==INF:
                continue
            dist[i]=min(dist[i], graph[i][j]+dist[j])

    return dist[0]


graph = ct.defaultdict(list)

graph[0]=[(1,1), (2,2), (3,5)]
graph[1]=[(4,4), (5,11)]
graph[2]=[(4,9), (5,5), (6,16)]
graph[3]=[(6,2)]
graph[4]=[(7,18)]
graph[5]=[(7,13)]
graph[6]=[(7,2)]

dist=[0]*8
for u in reversed(sorted(graph.keys())):
    dist[u]=INF
    for node, weight in graph[u]:
        print(u, '--', node, '=', weight)
        dist[u]=min(dist[u], weight+dist[node])

print(dist[0])