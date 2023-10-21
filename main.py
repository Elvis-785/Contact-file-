contacts = {}

def displayContacts():
    print("Name\t\tContact Number")
    for key in contacts:
        print("{}\t\t{}".format(key, contacts.get(key)))
while True:
    user_choice = int(input("""
1. Add new contact.
2. Search contacts.
3. Display contacts.
4. Edit contacts.
5. Delete contacts.
6. Exit\n 
"""))
    if user_choice == 1:
        name = input("Enter contact name:\n")
        phone = int(input("Enter phone number:\n"))
        contacts[name] = phone
    elif user_choice == 2:
        search_name = input("Enter contact name:\n")
        if search_name in contacts:
            print(search_name, "contact number is ", contacts[search_name])
        else:
            print("No contact was found.")
    elif user_choice == 3:
        if not contacts:
            print("The contact file is empty.")
        else:
            displayContacts()
    elif user_choice == 4:
        edit_contact = input("Enter contact name to be edited:\n")
        if edit_contact in contacts:
            phone_edit = int(input("Enter new phone number:\n"))
            contacts[edit_contact] = phone_edit
            print("updated successfully.")
            displayContacts()
        else:
            print("Name not found in the contact book.")
    elif user_choice == 5:
        del_contact = input("Enter contact name to be deleted: ")
        if del_contact in contacts:
            confirm = input("Do you want to delete this contact y or n:").lower()
            if confirm == "y":
                contacts.pop(del_contact)
            displayContacts()
        else:
            print("Name not found in the contact book.")
    else:
        print("Exiting ...")
        break
