
def contact_book():
    """
    Contact management system using dictionaries
    Each contact: {"name": str, "phone": str, "email": str, "category": str}
    """
    
    # Initialize empty contacts dictionary
    # Key: contact name (string), Value: contact info (dictionary)
    contacts = {
        "John Doe": {"phone": "123-456-7890", "email": "john@example.com", "category": "friend"},
        "Jane Smith": {"phone": "987-654-3210", "email": "jane@example.com", "category": "work"},
    }
    
    def add_contact():
        """Add a new contact to the address book"""
        print("\n=== Add New Contact ===")
        
        # Get contact information from user
        name = input("Enter contact name: ").strip()
        
        # TODO: Check if contact already exists
        if name in contacts:

            # If exists, ask user if they want to update    
            print("This contact is already exists.\nDo you want to updates.")
            condition = input("Yes or No : ").strip().lower()
            if condition != "yes":
                return
        
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()
        category = input("Enter category (family/friend/work/other): ").strip().lower()
        # TODO: Create contact dictionary and add to contacts
        dict = {}
        dict["phone"] = phone
        dict["email"] = email
        dict["category"] = category
        print(dict)

        # TODO: Add contact to the contacts dictionary
        contacts.update(name)
        print(f"Contact '{name}' added successfully!")
        print(contacts)
        
        
        
    
    
    def view_contact():
        """View details of a specific contact"""
        print("\n=== View Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to view: ").strip()
        
        # TODO: Check if contact exists and display information
        if name in contacts :
        # Format the output nicely
            info = contacts[name]
            print(f"name : {name} ")
            print(f"phone : {info["phone"]}")
            print(f"email : {info["email"]}")
            print(f"category : {info["category"]}")

        else :
            print("contacts not found!")
            pass
    
    def search_contacts():
        """Search contacts by name, phone, or email"""
        print("\n=== Search Contacts ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        search_term = input("Enter search term (name/phone/email): ").strip().lower()
        found_contacts = []

        # TODO: Search through all contacts
        for name,info in contacts:
            if (search_term in name.lower() or search_term in info["phone"] or search_term in info["email"].lower 
                or search_term in info["category"].lower) :
                found_contacts.append((name,info))
                
        # Check if search term appears in name, phone, or email

        # TODO: Implement search logic
        
        if found_contacts:
            print(f"\nFound {len(found_contacts)} contact(s):")
            # TODO: Display found contacts
        else:
            print("No contacts found matching your search.")
    
    def list_all_contacts():
        """Display all contacts in a formatted way"""
        print("\n=== All Contacts ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        print(f"{'Name':<20} {'Phone':<15} {'Email':<25} {'Category':<10}")
        print("-" * 70)
        
        # TODO: Implement listing logic
        
        pass
    
    def update_contact():
        """Update an existing contact"""
        print("\n=== Update Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to update: ").strip()
        
        # TODO: Check if contact exists
        # If exists, show current information
        # Ask what field to update
        # Update the contact information
        
        pass
    
    def delete_contact():
        """Delete a contact"""
        print("\n=== Delete Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to delete: ").strip()
        
        # TODO: Check if contact exists
        # Ask for confirmation
        # Delete the contact
        
        pass
    
    # Main menu loop
    while True:
        print("\n" + "="*50)
        print("           CONTACT BOOK MANAGER")
        print("="*50)
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contacts")
        print("4. List All Contacts")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            list_all_contacts()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            print("Thank you for using Contact Book Manager!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-7.")

if __name__ == "__main__":
    print("Starting Contact Book Manager...")
    
    contact_book()