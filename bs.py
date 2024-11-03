# Binary Search Tree Implementation
from binarytree import Node

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def insert_front(self, data):
        new_node = Node(data)
        new_node.left = self.root
        self.root = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                return
            elif not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    def delete_front(self):
        if not self.root:
            print("The tree is empty. No node to delete.")
            return
        # Replace root with the deepest node's value
        deepest_node = self._get_deepest_node()
        self.root.data = deepest_node.data
        self.delete_deepest()

    def delete_end(self):
        if not self.root:
            print("The tree is empty. No node to delete.")
            return
        if not self.root.left and not self.root.right:
            self.root = None
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left:
                if not current.left.left and not current.left.right:
                    current.left = None
                    return
                queue.append(current.left)
            if current.right:
                if not current.right.left and not current.right.right:
                    current.right = None
                    return
                queue.append(current.right)

    def _get_deepest_node(self):
        queue = [self.root]
        last = None
        while queue:
            last = queue.pop(0)
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)
        return last

    def display(self):
        if not self.root:
            print("The tree is empty.")
            return
        print(self.root)

def display_menu():
    print("\nBinary Tree Operations Menu:")
    print("1. Display the binary tree")
    print("2. Insert a node at the front")
    print("3. Insert a node at the end")
    print("4. Delete the root node")
    print("5. Delete the last node")
    print("6. Exit")

def main():
    # Create a binary tree
    root = Node(3)
    tree = BinaryTree(root)

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            tree.display()
        elif choice == '2':
            element = int(input("Enter a value to insert at the front: "))
            tree.insert_front(element)
            print(f"Element {element} inserted at the front of the binary tree.")
        elif choice == '3':
            element = int(input("Enter a value to insert at the end: "))
            tree.insert_end(element)
            print(f"Element {element} inserted at the end of the binary tree.")
        elif choice == '4':
            tree.delete_front()
            print("Root node deleted.")
        elif choice == '5':
            tree.delete_end()
            print("Last node deleted.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
