# Initialize an empty list to store the inventory
inventory = []

# Function to add a new product to the inventory
def add_product():
    product_name = input("Enter the product name: ")
    product_id = input("Enter the product ID: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    
    # Create a dictionary to store product details
    product = {
        "name": product_name,
        "id": product_id,
        "quantity": quantity,
        "price": price
    }
    
    # Add the product dictionary to the inventory list
    inventory.append(product)
    print(f"Product '{product_name}' added to the inventory.")

# Function to view the current inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        for product in inventory:
            print(f"ID: {product['id']}, Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")

# Function to update the quantity of an existing product
def update_product_quantity():
    product_id = input("Enter the product ID to update: ")
    
    for product in inventory:
        if product['id'] == product_id:
            new_quantity = int(input("Enter the new quantity: "))
            product['quantity'] = new_quantity
            print(f"Quantity for product ID '{product_id}' updated to {new_quantity}.")
            return
    
    print("Product ID not found.")

# Function to remove a product from the inventory
def remove_product():
    product_id = input("Enter the product ID to remove: ")
    
    for product in inventory:
        if product['id'] == product_id:
            inventory.remove(product)
            print(f"Product ID '{product_id}' removed from inventory.")
            return
    
    print("Product ID not found.")

# Main function to drive the program
def main():
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add a New Product")
        print("2. View Inventory")
        print("3. Update Product Quantity")
        print("4. Remove a Product")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_product_quantity()
        elif choice == '4':
            remove_product()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
