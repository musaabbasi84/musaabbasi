def get_income():
    while True:
        try:
            income = float(input("Enter your total income: "))
            return income
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_expenses():
    expenses = []
    print("Enter your expenses one by one. Enter 'done' when finished.")
    while True:
        expense = input("Enter an expense (or 'done' to finish): ")
        if expense.lower() == 'done':
            break
        try:
            amount = float(input("Enter the expense amount: "))
            expenses.append((expense, amount))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return expenses

def calculate_total_income(income):
    return sum(income)

def calculate_total_expenses(expenses):
    return sum(amount for _, amount in expenses)

def calculate_remaining_amount(income, expenses):
    total_income = calculate_total_income(income)
    total_expenses = calculate_total_expenses(expenses)
    return total_income - total_expenses

def main():
    print("Welcome to the Budget Calculator App!")

    income = get_income()
    expenses = get_expenses()

    total_income = calculate_total_income(income)
    total_expenses = calculate_total_expenses(expenses)
    remaining_amount = calculate_remaining_amount(income, expenses)

    print("\n-------- Budget Summary --------")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Amount: ${remaining_amount:.2f}")
    print("-------------------------------")

if __name__ == "__main__":
    main()
