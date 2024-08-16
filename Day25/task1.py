def add_expense(expenses):
    """Function to add a new expense."""
    try:
        # Get user input for expense details
        amount = float(input("Enter the expense amount: "))
        if amount <= 0:
            raise ValueError("The amount must be positive.")

        category = input("Enter the category (e.g., food, transportation, entertainment): ").strip().lower()
        description = input("Enter a description of the expense: ").strip()

        # Append the expense as a dictionary to the list
        expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })
        print("Expense added successfully.")

    except ValueError as e:
        print(f"Invalid input: {e}")

def display_summary(expenses):
    """Function to display a summary of expenses."""
    # Initialize a dictionary to hold the total spending per category
    summary = {}

    # Calculate total spending per category
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    # Display the summary
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category.title()}: ${total:.2f}")

def main():
    """Main function to manage the flow of the program."""
    expenses = []

    while True:
        # Display the menu
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        # Get user's choice
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            display_summary(expenses)
        elif choice == "3":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main function to start the program
if __name__ == "__main__":
    main()
