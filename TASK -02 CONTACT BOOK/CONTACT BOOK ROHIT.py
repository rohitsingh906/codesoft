contacts = []  # List to store contacts

def add_contact():
  name = input("Enter contact name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email (optional): ")
  contact = {"name": name, "phone": phone, "email": email}
  contacts.append(contact)

def view_contacts():
  if contacts:
    for i, contact in enumerate(contacts):
      print(f"{i+1}. {contact['name']} - {contact['phone']}")
      if contact.get("email"):
        print(f"      Email: {contact['email']}")
  else:
    print("No contacts found.")

def search_contacts():
  term = input("Enter search term: ")
  found = [contact for contact in contacts if term.lower() in contact["name"].lower()]
  if found:
    for i, contact in enumerate(found):
      print(f"{i+1}. {contact['name']} - {contact['phone']}")
      if contact.get("email"):
        print(f"      Email: {contact['email']}")
  else:
    print("No contacts found matching the term.")

def edit_contact():
  if contacts:
    index = int(input("Enter contact number to edit (1-{}: ".format(len(contacts)))) - 1
    if 0 <= index < len(contacts):
      contact = contacts[index]
      name = input("Update name (or leave blank to keep): ") or contact["name"]
      phone = input("Update phone number (or leave blank to keep): ") or contact["phone"]
      email = input("Update email (or leave blank to keep): ") or contact.get("email", "")
      contacts[index] = {"name": name, "phone": phone, "email": email}
      print("Contact updated.")
    else:
      print("Invalid contact number.")
  else:
    print("No contacts to edit.")

def delete_contact():
  if contacts:
    index = int(input("Enter contact number to delete (1-{}: ".format(len(contacts)))) - 1
    if 0 <= index < len(contacts):
      del contacts[index]
      print("Contact deleted.")
    else:
      print("Invalid contact number.")
  else:
    print("No contacts to delete.")

# Main loop for user interaction
while True:
  print("\nContact Book")
  print("1. Add Contact")
  print("2. View Contacts")
  print("3. Search Contacts")
  print("4. Edit Contact")
  print("5. Delete Contact")
  print("6. Exit")

  choice = input("Enter your choice (1-6): ")

  if choice == '1':
    add_contact()
  elif choice == '2':
    view_contacts()
  elif choice == '3':
    search_contacts()
  elif choice == '4':
    edit_contact()
  elif choice == '5':
    delete_contact()
  elif choice == '6':
    break
  else:
    print("Invalid choice. Please try again.")
