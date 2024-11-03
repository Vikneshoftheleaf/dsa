from sys import maxsize
from itertools import permutations

def travellingSalesmanProblem(graph, s):
    V = len(graph)
    vertex = [i for i in range(V) if i != s]
    min_path = maxsize
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]  # Return to the source vertex
        min_path = min(min_path, current_pathweight)

    return min_path

def get_graph_from_input():
    try:
        n = int(input("Enter the number of vertices (N): "))
        graph = []
        print("Enter the adjacency matrix (each row separated by newline, values separated by spaces):")
        
        for i in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                raise ValueError("The number of columns does not match the number of vertices.")
            graph.append(row)
        
        return graph
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def display_menu():
    print("\nMenu:")
    print("1. Solve Traveling Salesman Problem")
    print("2. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            graph = get_graph_from_input()
            if graph is not None:
                try:
                    s = int(input("Enter the starting vertex (0-indexed): "))
                    if s < 0 or s >= len(graph):
                        raise ValueError("Starting vertex is out of bounds.")
                    print("Minimum cost of traveling salesman tour:", travellingSalesmanProblem(graph, s))
                except ValueError as e:
                    print(f"Invalid input: {e}")
        
        elif choice == '2':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
