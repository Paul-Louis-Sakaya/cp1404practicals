

name = input("Enter name: ")

choice = ''
while choice != 'Q':
    print("\nMenu:")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    choice = input("Enter your choice: ").upper()

    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    elif choice == 'Q':
        print("Finished.")
    else:
        print("Invalid choice.")
