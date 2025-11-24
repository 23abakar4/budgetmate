"""
BudgetMate by Abubakar
A simple budget tracker that records expenses, shows summaries,
and helps manage money wisely.
"""

from datetime import datetime

# Store expenses in a list
expenses = []

# Function to add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g. Food, Transport): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    note = input("Enter a note (optional): ")
    
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }
    expenses.append(expense)
    print("✅ Expense added successfully!")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("📭 No expenses recorded yet.")
        return
    print("\n📋 Your Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | GHS {exp['amount']:.2f} | {exp['note']}")

# Function to show total summary
def show_summary():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Expenses: GHS {total:.2f}")

# Main menu loop
def main():
    while True:
        print("\n--- 🧮 BudgetMate Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("👋 Goodbye, Abubakar!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the program
main()
