def display_menu():
    print("\nStack Operations Menu:")
    print("1. Push an element")
    print("2. Pop an element")
    print("3. Peek at the top element")
    print("4. Display stack")
    print("5. Display stack length")
    print("6. Exit")

def main():
    stack = []
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            element = int(input("Enter an element to push: "))
            stack.append(element)
            print(f"Element {element} pushed to stack.")

        elif choice == '2':
            if stack:
                removed_element = stack.pop()
                print(f"Element {removed_element} popped from stack.")
            else:
                print("Stack is empty. Nothing to pop.")

        elif choice == '3':
            if stack:
                print(f"Top element is: {stack[-1]}")
            else:
                print("Stack is empty. No top element.")

        elif choice == '4':
            if stack:
                print("Stack:", stack)
            else:
                print("Stack is empty.")

        elif choice == '5':
            print("Stack length:", len(stack))

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
