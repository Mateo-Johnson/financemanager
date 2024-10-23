class UI:
    def show_main_menu(self):
        print("\nPersonal Finance Manager")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

    def show_user_menu(self):
        print("\nUser Menu")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Savings Goal")
        print("4. Add Budget")
        print("5. View Incomes")
        print("6. View Expenses")
        print("7. View Savings Goals")
        print("8. View Budgets")
        print("9. View Balance")
        print("10. View Expenses by Category")
        print("11. Generate Monthly Report")
        print("12. Logout")

    def get_input(self, prompt):
        return input(prompt)

    def display_items(self, items):
        if not items:
            print("No items to display.")
            return
        for item in items:
            print(item)

    def get_float_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_non_empty_input(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.")

    def get_username_password(self):
        username = self.get_non_empty_input("Enter username: ")
        password = self.get_non_empty_input("Enter password: ")
        return username, password
