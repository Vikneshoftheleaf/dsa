# Merge Sort Implementation

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged

def display_menu():
    print("\nMenu:")
    print("1. Enter a new list")
    print("2. Sort the list using merge sort")
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
                sorted_list = merge_sort(my_list)
                print("Sorted list:", sorted_list)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
