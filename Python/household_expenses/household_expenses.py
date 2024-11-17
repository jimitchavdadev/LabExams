import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

EXPENSES_FILE = 'expenses.csv'


def log_expense():
    """Log a new expense."""
    name = input("Enter your name: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category (e.g., groceries, utilities, entertainment): ")

    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date, description, amount, category])
    print("Expense logged successfully!")


def analyze_expenses():
    """Analyze expenses and display total and average expenses."""
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return

    total_expenses = defaultdict(float)
    total_days = defaultdict(int)

    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            amount = float(row['Amount'])
            total_expenses[name] += amount
            total_days[name] += 1

    print("\nTotal Expenses:")
    for name, total in total_expenses.items():
        average = total / total_days[name]
        print(f"{name}: Total = ${total:.2f}, Average = ${average:.2f}")

    household_total = sum(total_expenses.values())
    household_average = household_total / sum(total_days.values())
    print(f"\nHousehold Total Expenses: ${household_total:.2f}, Average Daily Expense: ${household_average:.2f}")


def plot_expense_trends():
    """Generate a line chart for expense trends over the last month."""
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return

    daily_expenses = defaultdict(float)

    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            date = row['Date']
            amount = float(row['Amount'])
            daily_expenses[date] += amount

    dates = sorted(daily_expenses.keys())
    amounts = [daily_expenses[date] for date in dates]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts, marker='o')
    plt.title("Daily Expenses Over the Last Month")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Expenses")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()


def categorize_expenses():
    """Categorize expenses and display breakdown by category."""
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return

    category_expenses = defaultdict(float)

    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            category_expenses[category] += amount

    print("\nExpenses by Category:")
    for category, total in category_expenses.items():
        print(f"{category}: Total = ${total:.2f}")


def monthly_expense_report():
    """Create a monthly expense report."""
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return

    monthly_expenses = defaultdict(lambda: defaultdict(float))

    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            amount = float(row['Amount'])
            date = datetime.strptime(row['Date'], '%Y-%m-%d')
            month = date.strftime('%Y-%m')
            monthly_expenses[month][name] += amount

    print("\nMonthly Expense Report:")
    for month, expenses in monthly_expenses.items():
        print(f"\nMonth: {month}")
        for name, total in expenses.items():
            print(f"{name}: Total = ${total:.2f}")


def set_monthly_budget():
    """Set monthly budget for each category and check against expenses."""
    budgets = {}
    while True:
        category = input("Enter the category to set a budget (or type 'done' to finish): ")
        if category.lower() == 'done':
            break
        budget = float(input(f"Enter the budget for {category}: "))
        budgets[category] = budget

    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return

    category_expenses = defaultdict(float)

    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            category_expenses[category] += amount

    print("\nBudget Status:")
    for category, budget in budgets.items():
        spent = category_expenses[category]
        remaining = budget - spent
        print(f"{category}: Budget = ${budget:.2f}, Spent = ${spent:.2f}, Remaining = ${remaining:.2f}")
        if remaining < 0:
            print(f"Warning: Budget exceeded for {category}!")


def backup_expenses():
    """Backup the expenses.csv file."""
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses file to backup.")
        return

    backup_file = 'expenses_backup.csv'
    with open(EXPENSES_FILE, 'r') as original:
        with open(backup_file, 'w') as backup:
            backup.write(original.read())
    print("Backup created successfully!")


def restore_expenses():
    """Restore the expenses.csv file from backup."""
    backup_file = 'expenses_backup.csv'
    if not os.path.exists(backup_file):
        print("No backup file found.")
        return

    with open(backup_file, 'r') as backup:
        with open(EXPENSES_FILE, 'w') as original:
            original.write(backup.read())
    print("Expenses restored from backup successfully!")


def main():
    while True:
        print("\n--- Household Expenses Tracker ---")
        print("1. Log Expense")
        print("2. Analyze Expenses")
        print("3. Plot Expense Trends")
        print("4. Categorize Expenses")
        print("5. Monthly Expense Report")
        print("6. Set Monthly Budget")
        print("7. Backup Expenses")
        print("8. Restore Expenses")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            log_expense()
        elif choice == '2':
            analyze_expenses()
        elif choice == '3':
            plot_expense_trends()
        elif choice == '4':
            categorize_expenses()
        elif choice == '5':
            monthly_expense_report()
        elif choice == '6':
            set_monthly_budget()
        elif choice == '7':
            backup_expenses()
        elif choice == '8':
            restore_expenses()
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()