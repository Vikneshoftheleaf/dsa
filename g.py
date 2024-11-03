# Graph Traversal using NetworkX
import networkx as nx

def create_graph():
    G = nx.Graph()
    nodes_input = input("Enter nodes separated by spaces: ")
    nodes = list(map(int, nodes_input.split()))
    G.add_nodes_from(nodes)
    
    edges_input = input("Enter edges as pairs (e.g., 1 2, 2 3): ")
    edges = [tuple(map(int, edge.split())) for edge in edges_input.split(', ')]
    G.add_edges_from(edges)
    return G

def perform_traversal(G):
    source = int(input("Enter the source node for traversal: "))
    dfs_result = list(nx.dfs_preorder_nodes(G, source=source))
    print("DFS Traversal:", dfs_result)
    bfs_result = list(nx.bfs_edges(G, source=source))
    print("BFS Traversal:", list(map(lambda x: x[1], bfs_result)))

def main():
    while True:
        print("\nMenu:")
        print("1. Create a new graph")
        print("2. Perform traversals on the graph")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            global G
            G = create_graph()
        elif choice == '2':
            if 'G' in globals():
                perform_traversal(G)
            else:
                print("Graph not created yet. Please create a graph first.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    G = None
    main()
