# B-Tree Implementation (using Red-Black Tree - FastRBTree)
from bintrees import FastRBTree

def display_menu():
    print("\nFastRBTree Operations Menu:")
    print("1. Insert a key-value pair")
    print("2. Print value for a specific key")
    print("3. Iterate over keys and values")
    print("4. Remove a key-value pair")
    print("5. Delete the minimum key (front)")
    print("6. Delete the maximum key (end)")
    print("7. Check if a key exists")
    print("8. Exit")

def main():
    btree = FastRBTree()

    while True:
        display_menu()
        choice = input("Choose an option (1-8): ")

        if choice == '1':
            key = int(input("Enter the key to insert: "))
            value = input("Enter the value to insert: ")
            btree[key] = value
            print(f"Key-value pair ({key}, {value}) inserted into the tree.")
        elif choice == '2':
            key = int(input("Enter the key to print its value: "))
            if key in btree:
                print(f"Value for key {key}: {btree[key]}")
            else:
                print(f"Key {key} not found in the tree.")
        elif choice == '3':
            print("Keys and values in sorted order:")
            for key, value in btree.items():
                print(f"Key: {key}, Value: {value}")
        elif choice == '4':
            key = int(input("Enter the key to remove: "))
            if key in btree:
                del btree[key]
                print(f"Key {key} removed from the tree.")
            else:
                print(f"Key {key} not found in the tree.")
        elif choice == '5':
            if btree:
                min_key = btree.min_key()
                del btree[min_key]
                print(f"Minimum key {min_key} removed from the tree.")
            else:
                print("The tree is empty. No key to delete.")
        elif choice == '6':
            if btree:
                max_key = btree.max_key()
                del btree[max_key]
                print(f"Maximum key {max_key} removed from the tree.")
            else:
                print("The tree is empty. No key to delete.")
        elif choice == '7':
            key = int(input("Enter the key to check if it exists: "))
            print(f"Key {key} exists in the tree." if key in btree else f"Key {key} does not exist in the tree.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()
