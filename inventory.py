class InventorySystem:
    def __init__(self):
        
        self.inventory = {
            "Laptop": {"price": 999.99, "quantity": 10},
            "Smartphone": {"price": 499.99, "quantity": 15},
            "Headphones": {"price": 129.99, "quantity": 20},
            "Monitor": {"price": 249.99, "quantity": 8},
            "Keyboard": {"price": 59.99, "quantity": 25}
        }

    def display_menu(self):
        """Display the main menu options."""
        print("\n===== Inventory Management System =====")
        print("1. Display all items")
        print("2. Add new item")
        print("3. Update item quantity")
        print("4. Update item price")
        print("5. Remove item")
        print("6. Search item")
        print("7. Exit")
        print("======================================")

    def display_all_items(self):
        
        print("\n----- Current Inventory -----")
        print(f"{'Item':<15} {'Price':<10} {'Quantity':<10}")
        print("-" * 35)
        
        if not self.inventory:
            print("Inventory is empty!")
        else:
            for item, details in self.inventory.items():
                print(f"{item:<15} ${details['price']:<9.2f} {details['quantity']:<10}")

    def add_item(self):
        
        item_name = input("Enter item name: ").strip()
        
        if item_name in self.inventory:
            print(f"Item '{item_name}' already exists in inventory!")
            return
        
        try:
            price = float(input("Enter item price: $"))
            quantity = int(input("Enter item quantity: "))
            
            if price < 0 or quantity < 0:
                print("Price and quantity must be positive values!")
                return
                
            self.inventory[item_name] = {"price": price, "quantity": quantity}
            print(f"Item '{item_name}' added successfully!")
        
        except ValueError:
            print("Invalid input! Price must be a number and quantity must be an integer.")

    def update_quantity(self):
        
        item_name = input("Enter item name to update quantity: ").strip()
        
        if item_name not in self.inventory:
            print(f"Item '{item_name}' not found in inventory!")
            return
        
        try:
            quantity = int(input("Enter new quantity: "))
            
            if quantity < 0:
                print("Quantity must be a positive value!")
                return
                
            self.inventory[item_name]["quantity"] = quantity
            print(f"Quantity for '{item_name}' updated successfully!")
        
        except ValueError:
            print("Invalid input! Quantity must be an integer.")

    def update_price(self):
       
        item_name = input("Enter item name to update price: ").strip()
        
        if item_name not in self.inventory:
            print(f"Item '{item_name}' not found in inventory!")
            return
        
        try:
            price = float(input("Enter new price: $"))
            
            if price < 0:
                print("Price must be a positive value!")
                return
                
            self.inventory[item_name]["price"] = price
            print(f"Price for '{item_name}' updated successfully!")
        
        except ValueError:
            print("Invalid input! Price must be a number.")

    def remove_item(self):
        
        item_name = input("Enter item name to remove: ").strip()
        
        if item_name not in self.inventory:
            print(f"Item '{item_name}' not found in inventory!")
            return
        
        del self.inventory[item_name]
        print(f"Item '{item_name}' removed successfully!")

    def search_item(self):

        item_name = input("Enter item name to search: ").strip()
        
        if item_name not in self.inventory:
            print(f"Item '{item_name}' not found in inventory!")
            return
        
        details = self.inventory[item_name]
        print(f"\nItem: {item_name}")
        print(f"Price: ${details['price']:.2f}")
        print(f"Quantity: {details['quantity']}")

    def run(self):
        
        while True:
            self.display_menu()
            try:
                print("\nEnter your choice (1-7): ", end="")
                choice = input()
                
                if choice == "1":
                    self.display_all_items()
                elif choice == "2":
                    self.add_item()
                elif choice == "3":
                    self.update_quantity()
                elif choice == "4":
                    self.update_price()
                elif choice == "5":
                    self.remove_item()
                elif choice == "6":
                    self.search_item()
                elif choice == "7":
                    print("\nExiting Inventory Management System. Goodbye!")
                    break
                else:
                    print("\nInvalid choice! Please enter a number between 1 and 7.")
            except EOFError:
                print("\nInput error occurred. Please try again.")
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Exiting...")
                break


if __name__ == "__main__":
    inventory_system = InventorySystem()
    inventory_system.run()