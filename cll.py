# Circular Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

def display_menu():
    print("\nCircular Linked List Operations Menu:")
    print("1. Append an element (Insert at end)")
    print("2. Prepend an element")
    print("3. Display the circular linked list")
    print("4. Exit")

def main():
    cll = CircularLinkedList()
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            element = int(input("Enter an element to append: "))
            cll.append(element)
            print(f"Element {element} appended to the circular linked list.")
        elif choice == '2':
            element = int(input("Enter an element to prepend: "))
            cll.prepend(element)
            print(f"Element {element} prepended to the circular linked list.")
        elif choice == '3':
            print("Circular Linked List:")
            cll.display()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
