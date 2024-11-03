import itertools

def is_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == j - i:
                return False
    return True

def solve_nqueens(n):
    solutions = []
    for permutation in itertools.permutations(range(n)):
        if is_valid(permutation):
            solutions.append(permutation)
    return solutions

def display_menu():
    print("\nMenu:")
    print("1. Solve N-Queens problem")
    print("2. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            try:
                n = int(input("Enter the board size (N): "))
                if n < 1:
                    print("The board size must be at least 1.")
                    continue
                solutions = solve_nqueens(n)
                print(f"Number of solutions for {n}-Queens problem: {len(solutions)}")
                for solution in solutions:
                    print(solution)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        elif choice == '2':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
