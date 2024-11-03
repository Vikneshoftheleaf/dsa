# AVL Tree Implementation
from avl import AVLTree

def display_menu():
    print("\nAVL Tree Operations Menu:")
    print("1. Insert an element")
    print("2. Display in-order traversal")
    print("3. Search for an element")
    print("4. Remove an element")
    print("5. Display height of the tree")
    print("6. Exit")

def main():
    avl_tree = AVLTree()
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            element = int(input("Enter an element to insert: "))
            avl_tree.insert(element)
            print(f"Element {element} inserted into the AVL tree.")
        elif choice == '2':
            print("In-order traversal:", avl_tree.in_order())
        elif choice == '3':
            element = int(input("Enter an element to search for: "))
            found = avl_tree.search(element)
            print(f"Found {element} in the tree." if found else f"{element} not found in the tree.")
        elif choice == '4':
            element = int(input("Enter an element to remove: "))
            avl_tree.remove(element)
            print(f"Element {element} removed from the AVL tree.")
        elif choice == '5':
            print("Height of the tree:", avl_tree.get_height(avl_tree.root))
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
