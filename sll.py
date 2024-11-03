
# Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        new_node = Node(data)
        if self.last_node is None:
            self.head = new_node
            self.last_node = self.head
        else:
            self.last_node.next = new_node
            self.last_node = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print("None")

    def is_empty(self):
        return self.head is None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.last_node is None:
            self.last_node = new_node

    def insert_end(self, data):
        self.append(data)

    def insert_middle(self, data, position):
        if position < 1:
            print("Invalid position. Position must be 1 or greater.")
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            if self.last_node is None:
                self.last_node = new_node
            return
        current = self.head
        count = 1
        while current is not None and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of bounds. Node not inserted.")
            return
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.last_node = new_node

def display_menu():
    print("\nLinked List Operations Menu:")
    print("1. Append an element (Insert at end)")
    print("2. Insert an element at front")
    print("3. Insert an element at middle (by position)")
    print("4. Display the linked list")
    print("5. Exit")

def main():
    linked_list = LinkedList()
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            element = int(input("Enter an element to append: "))
            linked_list.append(element)
            print(f"Element {element} appended to the linked list.")
        elif choice == '2':
            element = int(input("Enter an element to insert at front: "))
            linked_list.insert_front(element)
            print(f"Element {element} inserted at front.")
        elif choice == '3':
            element = int(input("Enter an element to insert at middle: "))
            position = int(input("Enter the position: "))
            linked_list.insert_middle(element, position)
            print(f"Element {element} inserted at position {position}.")
        elif choice == '4':
            print("Linked List:")
            linked_list.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
