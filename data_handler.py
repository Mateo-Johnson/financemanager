import sqlite3
from models import Income, Expense, SavingsGoal, Budget, User

class DataHandler:
    def __init__(self, db_name='finance.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS incomes (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    amount REAL NOT NULL,
                    source TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS savings_goals (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    target_amount REAL NOT NULL,
                    description TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS budgets (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    category TEXT NOT NULL,
                    limit REAL NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            ''')

    def add_user(self, user):
        with self.connection:
            self.connection.execute('''
                INSERT INTO users (username, password) VALUES (?, ?)
            ''', (user.username, user.password))

    def get_user(self, username):
        with self.connection:
            return self.connection.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

    def add_income(self, income, user_id):
        with self.connection:
            self.connection.execute('''
                INSERT INTO incomes (user_id, amount, source) VALUES (?, ?, ?)
            ''', (user_id, income.amount, income.source))

    def add_expense(self, expense, user_id):
        with self.connection:
            self.connection.execute('''
                INSERT INTO expenses (user_id, amount, category) VALUES (?, ?, ?)
            ''', (user_id, expense.amount, expense.category))

    def add_savings_goal(self, savings_goal, user_id):
        with self.connection:
            self.connection.execute('''
                INSERT INTO savings_goals (user_id, target_amount, description) VALUES (?, ?, ?)
            ''', (user_id, savings_goal.target_amount, savings_goal.description))

    def add_budget(self, budget, user_id):
        with self.connection:
            self.connection.execute('''
                INSERT INTO budgets (user_id, category, limit) VALUES (?, ?, ?)
            ''', (user_id, budget.category, budget.limit))

    def get_incomes(self, user_id):
        with self.connection:
            return self.connection.execute('SELECT * FROM incomes WHERE user_id = ?', (user_id,)).fetchall()

    def get_expenses(self, user_id):
        with self.connection:
            return self.connection.execute('SELECT * FROM expenses WHERE user_id = ?', (user_id,)).fetchall()

    def get_savings_goals(self, user_id):
        with self.connection:
            return self.connection.execute('SELECT * FROM savings_goals WHERE user_id = ?', (user_id,)).fetchall()

    def get_budgets(self, user_id):
        with self.connection:
            return self.connection.execute('SELECT * FROM budgets WHERE user_id = ?', (user_id,)).fetchall()

    def get_balance(self, user_id):
        total_income = sum(row[2] for row in self.get_incomes(user_id))
        total_expense = sum(row[2] for row in self.get_expenses(user_id))
        return total_income - total_expense

    def get_expenses_by_category(self, user_id):
        with self.connection:
            return self.connection.execute('''
                SELECT category, SUM(amount) FROM expenses WHERE user_id = ? GROUP BY category
            ''', (user_id,)).fetchall()

    def close(self):
        self.connection.close()
