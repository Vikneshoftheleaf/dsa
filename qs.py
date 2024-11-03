# Quick Sort Implementation

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def display_menu():
    print("\nMenu:")
    print("1. Enter a new list")
    print("2. Sort the list using quicksort")
    print("3. Exit")

def main():
    my_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            list_input = input("Enter the elements of the list separated by spaces: ")
            my_list = list(map(int, list_input.split()))
            print("List:", my_list)
        elif choice == '2':
            if not my_list:
                print("List is empty. Please enter a new list first.")
            else:
                sorted_list = quicksort(my_list)
                print("Sorted list:", sorted_list)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
