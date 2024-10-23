import matplotlib.pyplot as plt
import seaborn as sns
from data_handler import DataHandler

class ReportGenerator:
    def __init__(self, user_id):
        self.user_id = user_id
        self.data_handler = DataHandler()

    def generate_monthly_report(self):
        incomes = self.data_handler.get_incomes(self.user_id)
        expenses = self.data_handler.get_expenses(self.user_id)
        income_total = sum(row[2] for row in incomes)
        expense_total = sum(row[2] for row in expenses)

        print(f"\nMonthly Report")
        print(f"Total Income: ${income_total:.2f}")
        print(f"Total Expenses: ${expense_total:.2f}")
        print(f"Net Savings: ${income_total - expense_total:.2f}")

        self.visualize_expenses(expenses)

    def visualize_expenses(self, expenses):
        categories = [row[3] for row in expenses]
        amounts = [row[2] for row in expenses]

        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=categories, y=amounts)
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
