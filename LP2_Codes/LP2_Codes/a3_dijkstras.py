import sys

def minDistance(distances, visited):
    min_distance = sys.maxsize
    min_vertex = -1

    for v in range(len(distances)):
        if distances[v] < min_distance and not visited[v]:
            min_distance = distances[v]
            min_vertex = v

    return min_vertex

def dijkstra(graph, source):
    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    distances[source] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        u = minDistance(distances, visited)
        visited[u] = True

        for v in range(num_vertices):
            if graph[u][v] > 0 and not visited[v] and distances[u] + graph[u][v] < distances[v]:
                distances[v] = distances[u] + graph[u][v]

    return distances

# Take input from the user
num_vertices = int(input("Enter the number of vertices in the graph: "))
graph = [[0]* num_vertices for _ in range(num_vertices)]

num_edges = int(input("Enter the number of edges in the graph: "))
print("Enter the edges and weights in the format (u, v, weight):")
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    graph[u][v] = weight

source_vertex = int(input("Enter the source vertex: "))

shortest_distances = dijkstra(graph, source_vertex)

print("Shortest distances from source vertex", source_vertex)
for i in range(num_vertices):
    print("Vertex", i, ":", shortest_distances[i])
