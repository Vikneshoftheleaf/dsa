# Binary Tree Implementation
from binarytree import Node

def display_menu():
    print("\nBinary Tree Operations Menu:")
    print("1. Display the binary tree")
    print("2. Display list of nodes")
    print("3. Display inorder traversal")
    print("4. Display size of the tree")
    print("5. Display height of the tree")
    print("6. Display properties of the tree")
    print("7. Exit")

def main():
    # Create a binary tree
    root = Node(3)
    root.left = Node(6)
    root.right = Node(8)
    
    while True:
        display_menu()
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            print('Binary tree:', root)
        elif choice == '2':
            print('List of nodes:', list(root))
        elif choice == '3':
            print('Inorder of nodes:', root.inorder)
        elif choice == '4':
            print('Size of tree:', root.size)
        elif choice == '5':
            print('Height of tree:', root.height)
        elif choice == '6':
            print('Properties of tree:\n', root.properties)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()
