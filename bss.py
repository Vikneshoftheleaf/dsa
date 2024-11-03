# Binary Search Implementation

def binary_search(array, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def display_menu():
    print("\nMenu:")
    print("1. Enter a new array")
    print("2. Search for an element in the array")
    print("3. Exit")

def main():
    array = []
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            array_input = input("Enter the elements of the array separated by spaces: ")
            array = list(map(int, array_input.split()))
            array.sort()
            print("Array:", array)
        elif choice == '2':
            if not array:
                print("Array is empty. Please enter a new array first.")
            else:
                x = int(input("Enter the element to search for: "))
                result = binary_search(array, x, 0, len(array) - 1)
                print(f"Element is present at index {result}" if result != -1 else "Element is not present in array")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
