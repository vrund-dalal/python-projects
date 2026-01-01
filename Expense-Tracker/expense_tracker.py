expenses = {}

print("Expense Tracker")

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category (food, travel, etc): ")
        amount = float(input("Enter amount: "))

        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        print("Expense added")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet")
        else:
            print("\nExpenses by category:")
            for category in expenses:
                print(category, ":", expenses[category])

    elif choice == "3":
        total = 0
        for amount in expenses.values():
            total += amount

        print("Total expense:", total)

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
