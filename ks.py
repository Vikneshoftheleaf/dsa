# Knapsack Problem (Dynamic Programming Approach)

def knapsack(wt, val, W, n, t):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack(wt, val, W - wt[n-1], n - 1, t),
                      knapsack(wt, val, W, n - 1, t))
        return t[n][W]
    else:
        t[n][W] = knapsack(wt, val, W, n - 1, t)
        return t[n][W]

def display_menu():
    print("\nMenu:")
    print("1. Enter knapsack data")
    print("2. Solve knapsack problem")
    print("3. Exit")

def main():
    global t
    weights = []
    values = []
    capacity = 0
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            weights_input = input("Enter the weights separated by spaces: ")
            values_input = input("Enter the values separated by spaces: ")
            capacity = int(input("Enter the capacity of the knapsack: "))
            weights = list(map(int, weights_input.split()))
            values = list(map(int, values_input.split()))
            n = len(weights)
            t = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
            print("Weights:", weights)
            print("Values:", values)
            print("Capacity:", capacity)
        elif choice == '2':
            if not weights or not values:
                print("Knapsack data is empty. Please enter the data first.")
            else:
                n = len(weights)
                result = knapsack(weights, values, capacity, n, t)
                print("Maximum value that can be obtained:", result)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
