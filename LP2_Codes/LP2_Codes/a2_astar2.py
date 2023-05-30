def astar(graph, start, goal, heuristic):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        open_set.sort(key=lambda x: x[0])
        current = open_set.pop(0)[1]
        if current == goal:
            return g_score[current]

        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic[neighbor]
                open_set.append((f_score, neighbor))

    return float('inf')

# Get user input for the graph
graph = {}
nodes = int(input("Enter the number of nodes in the graph: "))
for _ in range(nodes):
    node = input("Enter the node: ")
    edges = int(input("Enter the number of edges for node " + node + ": "))
    graph[node] = {}
    for _ in range(edges):
        neighbor, distance = input("Enter neighbor and distance: ").split()
        graph[node][neighbor] = int(distance)

# Get user input for the heuristic values
heuristic = {}
for node in graph:
    heuristic[node] = int(input("Enter the heuristic value for node " + node + ": "))

# Get user input for the start and goal cities
start_city = input("Enter the start city: ")
goal_city = input("Enter the goal city: ")

# Call the A* algorithm with user input
distance = astar(graph, start_city, goal_city, heuristic)

if distance != float('inf'):
    print("Distance between", start_city, "and", goal_city, "is:", distance)
else:
    print("No path found between", start_city, "and", goal_city)
