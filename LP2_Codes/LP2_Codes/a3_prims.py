import sys
def minKey(key, mstSet):
    min_val = sys.maxsize
    min_idx = -1

    for v in range(len(key)):
        if key[v] < min_val and not mstSet[v]:
            min_val = key[v]
            min_idx = v
    return min_idx

def primMST(graph):
    V = len(graph)
    key = [sys.maxsize] * V
    parent = [None] * V
    key[0] = 0
    mstSet = [False] * V

    for _ in range(V):
        u = minKey(key, mstSet)
        mstSet[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent

V = int(input("Enter the number of vertices in the graph: "))
graph = [[0] * V for _ in range(V)]


E = int(input("Enter the number of edges in the graph: "))
print("Enter the edges and weights in the format (u, v, weight):")
for _ in range(E):
    u, v, weight = map(int, input().split())
    graph[u][v] = weight
    graph[v][u] = weight

mst = primMST(graph)

print("Edges in the Minimum Spanning Tree:")
for i in range(1, len(mst)):
    print(f"{mst[i]} - {i}")
