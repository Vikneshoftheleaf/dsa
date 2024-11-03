
# Circular Queue Implementation
import queue

class CircularQueue:
    def __init__(self, max_size):
        self.queue = queue.Queue(maxsize=max_size)

    def enqueue(self, item):
        try:
            self.queue.put(item, block=False)
            return True
        except queue.Full:
            print("Queue full. Cannot enqueue item.")
            return False

    def dequeue(self):
        try:
            item = self.queue.get(block=False)
            return item
        except queue.Empty:
            print("Queue is empty. Cannot dequeue item.")
            return None

    def is_empty(self):
        return self.queue.empty()

    def is_full(self):
        return self.queue.full()

    def size(self):
        return self.queue.qsize()

def display_menu():
    print("\nCircular Queue Operations Menu:")
    print("1. Enqueue an element")
    print("2. Dequeue an element")
    print("3. Check if queue is empty")
    print("4. Check if queue is full")
    print("5. Display queue size")
    print("6. Exit")

def main():
    max_size = int(input("Enter the maximum size of the queue: "))
    cq = CircularQueue(max_size)

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            element = input("Enter an element to enqueue: ")
            cq.enqueue(element)
        elif choice == '2':
            item = cq.dequeue()
            if item is not None:
                print(f"Dequeued: {item}")
        elif choice == '3':
            print("Queue is empty." if cq.is_empty() else "Queue is not empty.")
        elif choice == '4':
            print("Queue is full." if cq.is_full() else "Queue is not full.")
        elif choice == '5':
            print("Queue size:", cq.size())
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
