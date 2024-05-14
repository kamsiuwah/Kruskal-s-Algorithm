# Function to find the root of node 'i' with path compression technique
def find(parent, i):
    # If node i is its own parent, it is the root; return i
    if parent[i] == i:
        return i
    # Otherwise, recursively find the root of node i's parent and apply path compression
    return find(parent, parent[i])

# Function to union (merge) two subsets containing x and y
def union(parent, rank, x, y):
    # Find roots of the sets that x and y are elements of
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Union by rank to keep tree as flat as possible
    if rank[xroot] < rank[yroot]:
        # Make the tree with smaller rank a subtree of the tree with larger rank
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        # Make the tree with smaller rank a subtree of the tree with larger rank
        parent[yroot] = xroot
    else:
        # If ranks are the same, make one root the parent of the other and increase its rank
        parent[yroot] = xroot
        rank[xroot] += 1

# Function to perform Kruskal's algorithm to find the MST of a graph
def kruskal_mst(graph):
    result = []  # This list will store the resultant MST
    # Sort all edges in non-decreasing order of their weight
    edges = sorted(graph, key=lambda item: item[2])
    
    # Determine the maximum index vertex for initializing the union-find data structure
    max_vertex = max(max(u, v) for u, v, _ in edges) + 1
    
    # Initialize parent and rank for each vertex
    parent = list(range(max_vertex))
    rank = [0] * max_vertex
    
    e = 0  # Initial count of edges in MST
    i = 0  # Index for iterating through the sorted edge list

    # Process edges in sorted order until the MST contains max_vertex-1 edges
    while e < max_vertex - 1:
        u, v, w = edges[i]
        i += 1
        # Find the roots of the vertices u and v
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does not cause a cycle
        if x != y:
            e += 1  # Increment the count of MST edges
            result.append((u, v, w))  # Add the edge to the result
            # Union the sets of u and v
            union(parent, rank, x, y)

    # Return the list of edges in the MST
    return result

# Function to print the results of Kruskal's MST algorithm
def print_mst_results(graph, graph_type):
    print(f"\nResults for {graph_type} graph using Kruskal's algorithm:")
    # Generate the MST using Kruskal's algorithm
    mst_kruskal = kruskal_mst(graph)
    # Calculate the total weight of the MST
    total_weight_kruskal = sum(w for _, _, w in mst_kruskal)
    print("MST:", mst_kruskal)
    print("Total Weight:", total_weight_kruskal)

# Example graphs in the form of lists of edges (u, v, weight)
sparse_graph_edges = [(0, 1, 1), (1, 2, 3)]
dense_graph_edges = [(0, 1, 2), (0, 2, 4), (0, 3, 1), (1, 2, 3), (1, 3, 5), (2, 3, 1)]
varied_weights_graph_edges = [(0, 1, 10), (0, 2, 20), (1, 2, 15), (2, 3, 5)]

# Print MST results for different graph types
print_mst_results(sparse_graph_edges, "Sparse")
print_mst_results(dense_graph_edges, "Dense")
print_mst_results(varied_weights_graph_edges, "Varied Weights")
