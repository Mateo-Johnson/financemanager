class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(username='{self.username}')"

class Income:
    def __init__(self, amount, source):
        self.amount = amount
        self.source = source

    def __repr__(self):
        return f"Income(amount={self.amount}, source='{self.source}')"

class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f"Expense(amount={self.amount}, category='{self.category}')"

class SavingsGoal:
    def __init__(self, target_amount, description):
        self.target_amount = target_amount
        self.description = description

    def __repr__(self):
        return f"SavingsGoal(target_amount={self.target_amount}, description='{self.description}')"

class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit

    def __repr__(self):
        return f"Budget(category='{self.category}', limit={self.limit})"
