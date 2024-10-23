from data_handler import DataHandler
from models import Income, Expense, SavingsGoal, Budget, User
from ui import UI
from report_generator import ReportGenerator

def main():
    data_handler = DataHandler()
    ui = UI()
    current_user = None

    while True:
        ui.show_main_menu()
        choice = ui.get_input("Choose an option: ")

        if choice == "1":
            username, password = ui.get_username_password()
            user = data_handler.get_user(username)
            if user and user[2] == password:
                current_user = user[0]
                print("Login successful.")
            else:
                print("Invalid username or password.")

        elif choice == "2":
            username, password = ui.get_username_password()
            try:
                data_handler.add_user(User(username, password))
                print("User registered successfully.")
            except sqlite3.IntegrityError:
                print("Username already exists.")

        elif choice == "3":
            data_handler.close()
            print("Exiting the program.")
            break

        if current_user is not None:
            while True:
                ui.show_user_menu()
                user_choice = ui.get_input("Choose an option: ")

                if user_choice == "1":
                    amount = ui.get_float_input("Enter income amount: ")
                    source = ui.get_non_empty_input("Enter income source: ")
                    data_handler.add_income(Income(amount, source), current_user)
                    print("Income added successfully.")

                elif user_choice == "2":
                    amount = ui.get_float_input("Enter expense amount: ")
                    category = ui.get_non_empty_input("Enter expense category: ")
                    data_handler.add_expense(Expense(amount, category), current_user)
                    print("Expense added successfully.")

                elif user_choice == "3":
                    target_amount = ui.get_float_input("Enter savings goal amount: ")
                    description = ui.get_non_empty_input("Enter savings goal description: ")
                    data_handler.add_savings_goal(SavingsGoal(target_amount, description), current_user)
                    print("Savings goal set successfully.")

                elif user_choice == "4":
                    category = ui.get_non_empty_input("Enter budget category: ")
                    limit = ui.get_float_input("Enter budget limit: ")
                    data_handler.add_budget(Budget(category, limit), current_user)
                    print("Budget added successfully.")

                elif user_choice == "5":
                    incomes = data_handler.get_incomes(current_user)
                    ui.display_items(incomes)

                elif user_choice == "6":
                    expenses = data_handler.get_expenses(current_user)
                    ui.display_items(expenses)

                elif user_choice == "7":
                    savings_goals = data_handler.get_savings_goals(current_user)
                    ui.display_items(savings_goals)

                elif user_choice == "8":
                    budgets = data_handler.get_budgets(current_user)
                    ui.display_items(budgets)

                elif user_choice == "9":
                    balance = data_handler.get_balance(current_user)
                    print(f"Current Balance: ${balance:.2f}")

                elif user_choice == "10":
                    expenses_by_category = data_handler.get_expenses_by_category(current_user)
                    ui.display_items(expenses_by_category)

                elif user_choice == "11":
                    report_gen = ReportGenerator(current_user)
                    report_gen.generate_monthly_report()

                elif user_choice == "12":
                    current_user = None
                    print("Logged out successfully.")
                    break

                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
