# personal Contact manager
import json
import os
from datetime import datetime

class ContactManager:
    """A personal contact manager with file storage"""
    
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    return json.load(file)
            else:
                print("No existing contacts file found. Starting fresh.")
                return []
        except json.JSONDecodeError:
            print("Error reading contacts file. Starting with empty list.")
            return []
        except Exception as e:
            print(f"Error loading contacts: {e}")
            return []
    
    def save_contacts(self):
        """Save contacts to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.contacts, file, indent=4)
            print(f"Contacts saved successfully to {self.filename}")
            return True
        except Exception as e:
            print(f"Error saving contacts: {e}")
            return False
    
    def add_contact(self):
        """Add a new contact"""
        print("\n--- Add New Contact ---")
        try:
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            
            # Validate input
            if not name or not phone:
                print("Name and phone are required!")
                return
            
            contact = {
                'id': len(self.contacts) + 1,
                'name': name,
                'phone': phone,
                'email': email,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.contacts.append(contact)
            self.save_contacts()
            print(f"Contact '{name}' added successfully!")
            
        except Exception as e:
            print(f"Error adding contact: {e}")
    
    def view_contacts(self):
        """View all contacts"""
        print("\n--- All Contacts ---")
        if not self.contacts:
            print("No contacts found.")
            return
        
        for contact in self.contacts:
            print(f"ID: {contact['id']}")
            print(f" Name: {contact['name']}")
            print(f" Phone: {contact['phone']}")
            print(f" Email: {contact['email']}")
            print(f" Added: {contact['created_at']}")
            print("-" * 30)
    
    def search_contact(self):
        """Search for a contact"""
        print("\n--- Search Contact ---")
        search_term = input("Enter name or phone to search: ").strip().lower()
        
        results = []
        for contact in self.contacts:
            if (search_term in contact['name'].lower() or 
                search_term in contact['phone']):
                results.append(contact)
        
        if results:
            print(f"Found {len(results)} contact(s):")
            for contact in results:
                print(f" {contact['name']} - {contact['phone']}")
        else:
            print("No contacts found.")
    
    def delete_contact(self):
        """Delete a contact"""
        self.view_contacts()
        if not self.contacts:
            return
        
        try:
            contact_id = int(input("Enter ID of contact to delete: "))
            
            for i, contact in enumerate(self.contacts):
                if contact['id'] == contact_id:
                    removed = self.contacts.pop(i)
                    self.save_contacts()
                    print(f"Contact '{removed['name']}' deleted successfully!")
                    return
            
            print(f"No contact found with ID {contact_id}")
            
        except ValueError:
            print("Please enter a valid number!")
        except Exception as e:
            print(f"Error deleting contact: {e}")
    
    def export_contacts(self, format='csv'):
        """Export contacts to different formats"""
        try:
            if format == 'csv':
                with open('contacts_export.csv', 'w') as file:
                    file.write("ID,Name,Phone,Email,Created_At\n")
                    for contact in self.contacts:
                        file.write(f"{contact['id']},{contact['name']},"
                                 f"{contact['phone']},{contact['email']},"
                                 f"{contact['created_at']}\n")
                print("Contacts exported to CSV successfully!")
                
            elif format == 'txt':
                with open('contacts_export.txt', 'w') as file:
                    file.write("CONTACT LIST\n")
                    file.write("=" * 50 + "\n")
                    for contact in self.contacts:
                        file.write(f"ID: {contact['id']}\n")
                        file.write(f"Name: {contact['name']}\n")
                        file.write(f"Phone: {contact['phone']}\n")
                        file.write(f"Email: {contact['email']}\n")
                        file.write(f"Added: {contact['created_at']}\n")
                        file.write("-" * 30 + "\n")
                print("Contacts exported to TXT successfully!")
                
        except Exception as e:
            print(f"Error exporting contacts: {e}")
    
    def menu(self):
        """Display main menu"""
        while True:
            print("\n=== PERSONAL CONTACT MANAGER ===")
            print("1. Add Contact")
            print("2. View All Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Export Contacts (CSV)")
            print("6. Export Contacts (TXT)")
            print("7. Backup Contacts")
            print("8. Exit")
            
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                self.export_contacts('csv')
            elif choice == '6':
                self.export_contacts('txt')
            elif choice == '7':
                self.create_backup()
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def create_backup(self):
        """Create a backup of contacts file"""
        try:
            if os.path.exists(self.filename):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_name = f"contacts_backup_{timestamp}.json"
                shutil.copy2(self.filename, backup_name)
                print(f"Backup created: {backup_name}")
            else:
                print("No contacts file to backup.")
        except Exception as e:
            print(f"Error creating backup: {e}")

# Main program
if __name__ == "__main__":
    # Check if required modules are available
    try:
        import shutil
    except ImportError:
        print("shutil module not available. Some features may be limited.")
        shutil = None
    
    # Create and run contact manager
    manager = ContactManager()
    manager.menu()
