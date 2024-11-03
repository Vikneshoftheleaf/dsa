def display_menu():
    print("\nQueue Operations Menu:")
    print("1. Enqueue an element")
    print("2. Dequeue an element")
    print("3. Display queue")
    print("4. Exit")

def main():
    queue = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            element = input("Enter an element to enqueue: ")
            queue.append(element)
            print(f"Element {element} enqueued to queue.")

        elif choice == '2':
            if queue:
                removed_element = queue.pop(0)
                print(f"Element {removed_element} dequeued from queue.")
            else:
                print("Queue is empty. Nothing to dequeue.")

        elif choice == '3':
            if queue:
                print("Queue:", queue)
            else:
                print("Queue is empty.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
