def dfs(visited, graph, node):
    if node not in visited:
        print(node, " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)
    while queue:
        ele = queue.pop(0)
        print(ele, " ")
        for neighbour in graph[ele]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

visited1 = set()
visited2 = set()
queue = []
graph = {}

def create_graph():
    n = int(input("Number of nodes: "))
    for i in range(1, n + 1):
        edge = int(input("Enter the number of edges for node {}: ".format(i)))
        graph[i] = []
        for j in range(1, edge + 1):
            node = int(input("Enter the edge {} for node {}: ".format(j, i)))
            graph[i].append(node)

def menu():
    print("\nMenu:")
    print("1. Create graph")
    print("2. BFS")
    print("3. DFS")
    print("4. Quit")

while True:
    menu()
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        create_graph()
    
    elif choice == 2:
        start_node = int(input("Enter the start node for BFS: "))
        print("\nBFS:")
        bfs(visited1, graph, start_node, queue)
    
    elif choice == 3:
        start_node = int(input("Enter the start node for DFS: "))
        print("\nDFS:")
        dfs(visited2, graph, start_node)

    elif choice == 4:
        break
    
    else:
        print("Invalid choice. Please try again.")
