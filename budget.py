import string
import random

class Expense:
    def __init__(self, ID: str, category: str, amount: float, description: float, date: str):
        self.ID = ''
        self.category = category
        self.amount = amount
        self.description = description
        self.date = date

    def set_ID(self, ID: str):
        self.ID = ID

    def get_category(self):
        return self.category
    def get_amount(self):
        return self.amount
    def get_description(self):
        return self.description
    def get_date(self):
        return self.date
    
    def to_str(self):
        expense_str = f'{self.ID:5}|{self.category:5}|{self.amount:5.2f}|{self.description:20}|{self.date}'

class Budget:
    instance = None
    generated_IDs = set()

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.expenses: dict[str : Expense] = {}

    def add(self, expense: Expense):
        ID = Budget.generate_ID()
        self.expenses[ID] = expense
        expense.set_ID(ID)

    def remove(self, ID: str):
        if ID not in self.expenses:
            print(f'Error: No expense with ID {ID} in budget.')
        self.expenses.pop(ID)

    def list_expenses(self):
        print('Expenses:')
        for expense in self.expenses.values():
            print(expense.to_str())

    def summary(self, category: str):
        total = 0.0
        for expense in self.expenses.values():
            if expense.get_category() == category:
                total += expense.get_amount()
        print('Total expenses for {category}: {total:.2f}')

    def export(self):
        pass

    def generate_ID():
        ID = ''
        while True:
            ID = ''.join(random.choice(string.ascii_letters+ string.digits, k=4))
            if ID not in Budget.generated_IDs:
                break
        Budget.generated_IDs.add(ID)
        return ID