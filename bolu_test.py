def add_contact(contacts, name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for ids, contact in enumerate(contacts, start=1):
            print(f"Contact {ids}:\n"
                  f"Name: {contact['name']}\n"
                  f"Phone: {contact['phone']}\n"
                  f"Email: {contact['email']}\n")


def update_contact(contacts, index, name, phone, email):
    if index >= 0 and index < len(contacts):
        contacts[index] = {"name": name, "phone": phone, "email": email}
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Invalid index. Please view contacts to check the indexes.")


def delete_contact(contacts, index):
    if index >= 0 and index < len(contacts):
        deleted_contact = contacts.pop(index)
        save_contacts(contacts)
        print(f"Contact {deleted_contact['name']} deleted successfully.")
    else:
        print("Invalid index. Please view contacts to check the indexes.")


def save_contacts(contacts):
    with open("contacts.txt", "w") as f:
        for contact in contacts:
            f.write(f"Name: {contact['name']}\n"
                    f"Phone: {contact['phone']}\n"
                    f"Email: {contact['email']}\n"
                    f"{'=' * 20}\n")


def load_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as f:
            lines = f.read().split('=' * 20 + '\n')
            for line in lines:
                if line.strip():
                    fields = line.strip().split('\n')
                    name = fields[0].split(': ')[1]
                    phone = fields[1].split(': ')[1]
                    email = fields[2].split(': ')[1]
                    contacts.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        pass
    return contacts


contacts = load_contacts()

while True:
    print("\nWelcome to the contact Book Menu: \n1. Add Contact\n2. View Contacts\n3. Update Contact\n4. Delete Contact\n5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(contacts, name, phone, email)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        index = int(input("Enter the index of the contact to update: "))
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        update_contact(contacts, index - 1, name, phone, email)
    elif choice == "4":
        index = int(input("Enter the index of the contact to delete: "))
        delete_contact(contacts, index - 1)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

