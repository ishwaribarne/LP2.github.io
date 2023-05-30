#include <iostream>
#include <climits>

using namespace std;

// Function to find the vertex with the minimum key value
int minKey(int key[], bool mstSet[], int V)
{
    int minKey = INT_MAX, minIndex;

    for (int v = 0; v < V; v++)
    {
        if (!mstSet[v] && key[v] < minKey)
        {
            minKey = key[v];
            minIndex = v;
        }
    }

    return minIndex;
}

// Function to print the MST
void printMST(int parent[], int graph[][100], int V)
{
    cout << "Edge \tWeight\n";
    for (int i = 1; i < V; i++)
    {
        cout << parent[i] << " - " << i << "\t" << graph[i][parent[i]] << "\n";
    }
}

void primMST(int graph[][100], int V)
{
    int parent[V];            // Array to store constructed MST
    int key[V];               // Key values used to pick the minimum weight edge
    bool mstSet[V] = {false}; // To represent set of vertices not yet included in MST

    for (int i = 0; i < V; i++)
    {
        key[i] = INT_MAX;
    }

    key[0] = 0;
    parent[0] = -1;

    // MST will have V vertices
    for (int count = 0; count < V - 1; count++)
    {
        int u = minKey(key, mstSet, V);
        mstSet[u] = true;
        for (int v = 0; v < V; v++)
        {
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v])
            {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    printMST(parent, graph, V);
}

int main()
{
    int V;
    cout << "Enter the number of vertices in the graph: ";
    cin >> V;

    int graph[100][100];
    cout << "Enter the adjacency matrix of the graph:\n";
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            cin >> graph[i][j];
        }
    }

    primMST(graph, V);
    return 0;
}