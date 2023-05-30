def kruskal(graph):
    mst = []  # minimum spanning tree
    visited2 = set()  # for storing visited elements for cycle checking
    # visited = []
    edges = []
    
    for node in range(len(graph)):
        # visited.append(node)
        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] != 0:
                edges.append((graph[node][neighbor], node, neighbor))
    
    edges.sort()
    i = 0
    
    while i < len(edges):
        cost, frm, to = edges[i]
        if frm not in visited2 or to not in visited2:
            # if one of the nodes is not in visited2, they will not form a cycle
            mst.append((frm, to, cost))
            visited2.add(frm)
            visited2.add(to)
        i += 1
    
    return mst


graph = []
n = int(input("Enter the number of vertices: "))
print("Enter the adjacency matrix (space-separated values):")
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

mst = kruskal(graph)
for edge in mst:
    print(f"Edge: {edge[0]} - {edge[1]}, Cost: {edge[2]}")
