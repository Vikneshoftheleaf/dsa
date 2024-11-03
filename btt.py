# Binary Tree Traversal
from binarytree import Node

def display_menu():
    print("\nBinary Tree Operations Menu:")
    print("1. Display the binary tree")
    print("2. Display list of nodes")
    print("3. Display inorder traversal")
    print("4. Display preorder traversal")
    print("5. Display postorder traversal")
    print("6. Display size of the tree")
    print("7. Display height of the tree")
    print("8. Display properties of the tree")
    print("9. Exit")

def main():
    # Create a binary tree
    root = Node(3)
    root.left = Node(6)
    root.right = Node(8)

    while True:
        display_menu()
        choice = input("Choose an option (1-9): ")
        
        if choice == '1':
            print('Binary tree:', root)
        elif choice == '2':
            print('List of nodes:', list(root))
        elif choice == '3':
            print('Inorder traversal:', root.inorder)
        elif choice == '4':
            print('Preorder traversal:', root.preorder)
        elif choice == '5':
            print('Postorder traversal:', root.postorder)
        elif choice == '6':
            print('Size of tree:', root.size)
        elif choice == '7':
            print('Height of tree:', root.height)
        elif choice == '8':
            print('Properties of tree:\n', root.properties)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 9.")

if __name__ == "__main__":
    main()
