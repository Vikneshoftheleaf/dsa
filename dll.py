# Doubly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

def display_menu():
    print("\nDoubly Linked List Operations Menu:")
    print("1. Append an element (Insert at end)")
    print("2. Prepend an element")
    print("3. Display the doubly linked list")
    print("4. Exit")

def main():
    dll = DoublyLinkedList()
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            element = int(input("Enter an element to append: "))
            dll.append(element)
            print(f"Element {element} appended to the doubly linked list.")
        elif choice == '2':
            element = int(input("Enter an element to prepend: "))
            dll.prepend(element)
            print(f"Element {element} prepended to the doubly linked list.")
        elif choice == '3':
            print("Doubly Linked List:")
            dll.display()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
