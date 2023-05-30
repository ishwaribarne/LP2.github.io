import sys
# Function to find the vertex with the minimum distance value
def minDistance(distances, visited):
    min_dist = sys.maxsize
    min_vertex = None
    for v in range(len(distances)):
        if distances[v] < min_dist and not visited[v]:
            min_dist = distances[v]
            min_vertex = v
    return min_vertex

# Function to print the shortest path from source to target
def printPath(parents, target):
    if parents[target] is None:
        return
    printPath(parents, parents[target])
    print(target, end=" ")

# Function to find the shortest path from source to all other vertices
def dijkstra(graph, source):
    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    parents = [None] * num_vertices
    visited = [False] * num_vertices

    distances[source] = 0

    for _ in range(num_vertices - 1):
        u = minDistance(distances, visited)
        visited[u] = True

        for v in range(num_vertices):
            if (
                graph[u][v] > 0
                and not visited[v]
                and distances[v] > distances[u] + graph[u][v]
            ):
                distances[v] = distances[u] + graph[u][v]
                parents[v] = u

    # Print the shortest paths
    for v in range(num_vertices):
        if v != source:
            print(f"Shortest path from {source} to {v}: ", end="")
            printPath(parents, v)
            print(f"({distances[v]})")
    print()

    
num_vertices = int(input("Enter the number of vertices: "))
graph = [[0] * num_vertices for _ in range(num_vertices)]

num_edges = int(input("Enter the number of edges: "))
print("Enter the edges and their weights:")
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    graph[u][v] = weight

source = int(input("Enter the source vertex: "))

dijkstra(graph, source)