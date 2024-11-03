import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.DiGraph()
    # Collect nodes and edges from the user
    nodes_input = input("Enter nodes separated by commas (e.g., start, stage1a, stage1b): ")
    nodes = nodes_input.split(',')
    nodes = [node.strip() for node in nodes]
    G.add_nodes_from(nodes)
    
    edges_input = input("Enter edges separated by commas (e.g., start-stage1a, start-stage1b): ")
    edges = edges_input.split(',')
    edges = [tuple(edge.strip().split('-')) for edge in edges]
    G.add_edges_from(edges)
    
    return G

def display_graph(G):
    pos = nx.spring_layout(G)  # Create a layout for the nodes
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold")
    plt.show()

def display_menu():
    print("\nMenu:")
    print("1. Create a new graph")
    print("2. Display the graph")
    print("3. Exit")

def main():
    G = None
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            G = create_graph()
            print("Graph created successfully.")
        
        elif choice == '2':
            if G is None:
                print("No graph has been created yet. Please create a graph first.")
            else:
                display_graph(G)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
