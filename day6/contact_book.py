import json
import os

FILENAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    # basic duplicate check (same name and phone)
    for c in contacts:
        if c["name"].lower() == name.lower() and c["phone"] == phone:
            print("⚠️ Contact already exists. Skipping.")
            return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added!")

def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\nSaved Contacts:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")

def search_contact(contacts):
    query = input("Search by name or phone: ").strip().lower()
    found = [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"]
    ]
    if not found:
        print("No matching contact.")
        return
    print("\nSearch Results:")
    for c in found:
        print(f"- {c['name']} - {c['phone']} - {c['email']}")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("Enter contact number to delete: ").strip())
        if 1 <= idx <= len(contacts):
            removed = contacts.pop(idx - 1)
            save_contacts(contacts)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
