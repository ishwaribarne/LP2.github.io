def aStarAlgo(start_node, stop_node, graph):
    open_set = set([start_node])
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or (g[v] + heuristic(v) < g[n] + heuristic(n)):
                n = v

        if n == stop_node or graph[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n, graph):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

        if n == None:
            print('Path does not exist!')
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

def get_neighbors(v, graph):
    if v in graph:
        return graph[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        # 'A': 11,
        # 'B': 6,
        # 'C': 99,
        # 'D': 1,
        # 'E': 7,
        # 'G': 0,
        'B': 12,
        'C': 11,
        'D': 6,
        'E': 4,
        'G': 0,
        'S': 14,
        'F': 11
    }
    return H_dist[n]

def create_graph():
    n = int(input("Enter the number of nodes: "))
    graph = {}
    for i in range(n):
        node = input("Enter the node: ")
        edges = int(input("Enter the number of edges for node {}: ".format(node)))
        graph[node] = []
        for j in range(edges):
            neighbor = input("Enter neighbor {}: ".format(j+1))
            weight = int(input("Enter the weight for the edge: "))
            graph[node].append((neighbor, weight))
    return graph

def main():
    graph = create_graph()

    while True:
        print("\nMenu:")
        print("1. A* Algorithm")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            start_node = input("Enter the start node: ")
            stop_node = input("Enter the stop node: ")
            aStarAlgo(start_node, stop_node, graph)

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()