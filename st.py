INF = 9999999  # A large number representing infinity

def print_graph(G):
    print("\nAdjacency Matrix:")
    for row in G:
        print(" ".join(map(str, row)))
    print()

def prims_algorithm(G):
    N = len(G)
    selected_node = [False] * N
    no_edge = 0
    selected_node[0] = True  # Start from the first node
    print("Edge : Weight")
    
    while no_edge < N - 1:
        minimum = INF
        a = 0
        b = 0
        for m in range(N):
            if selected_node[m]:  # Only consider selected nodes
                for n in range(N):
                    if not selected_node[n] and G[m][n]:  # Not in selected and there is an edge
                        if minimum > G[m][n]:  # Find the minimum weight edge
                            minimum = G[m][n]
                            a = m
                            b = n
        print(f"{a}-{b}: {G[a][b]}")
        selected_node[b] = True  # Include this node in the MST
        no_edge += 1

def display_menu():
    print("\nMenu:")
    print("1. Enter adjacency matrix")
    print("2. Run Prim's algorithm")
    print("3. Exit")

def main():
    G = []
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Enter adjacency matrix
            print("Enter the adjacency matrix row by row (space-separated values).")
            G = []
            N = int(input("Enter the number of vertices: "))
            for i in range(N):
                row = list(map(int, input(f"Enter row {i + 1}: ").split()))
                G.append(row)
            print_graph(G)

        elif choice == '2':
            if not G:
                print("Adjacency matrix is empty. Please enter the matrix first.")
            else:
                prims_algorithm(G)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
