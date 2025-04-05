import os
import string
import random
import json
import csv

class Expense:
    def __init__(self, category: str, amount: float, description: str, date: str):
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
        expense_str = f'{self.ID:5}{self.category:10}{self.amount:<10.2f}{self.description:40}{self.date}'
        return expense_str

class Budget:
    instance = None
    generated_IDs = set()

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.expenses: dict[str : Expense] = {}

    def add(self, category : str, amount : float, description : str, date : str):
        expense = Expense(category, amount, description, date)
        ID = Budget.generate_ID()
        self.expenses[ID] = expense
        expense.set_ID(ID)
        print('Added expense to budget:')
        print(expense.to_str())

    def remove(self, ID: str):
        if ID not in self.expenses:
            print(f'Error: No expense with ID {ID} in budget.')
        self.expenses.pop(ID)
        print(f'Remove expense with ID {ID} from budget!')

    def list_expenses(self):
        if not self.expenses:
            print('No expenses in budget to list.')
            return
        print('Expenses:')
        print(f'{'ID':5}{'category':10}{'amount':10}{'description':40}{'date'}')
        for expense in self.expenses.values():
            print(expense.to_str())

    def summary(self, category: str):
        total = 0.0
        for expense in self.expenses.values():
            if expense.get_category() == category:
                total += expense.get_amount()
        print(f'Total expenses for {category}: {total:.2f}')

    def to_dict(self):
        data = {
            ID: {
                'category': expense.get_category(),
                'amount': expense.get_amount(),
                'description': expense.get_description(),
                'date': expense.get_date()
            }
            for ID, expense in self.expenses.items()
        }
        return data

    def export_csv(self, filename, directory):
        data = self.to_dict()
        filename += ".csv"
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            print(f'Error: a file with same name already exists at {filepath}.')
            return
        with open(filepath, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'category', 'amount', 'description', 'date'])
            for ID, expense in data.items():
                writer.writerow([ID, expense['category'], expense['amount'], expense['description'], expense['date']])
        print(f"Export budget as csv to {filepath}")

    def generate_ID():
        ID = ''
        while True:
            ID = ''.join(random.choices(string.ascii_letters+ string.digits, k=4))
            if ID not in Budget.generated_IDs:
                break
        Budget.generated_IDs.add(ID)
        return ID

    def save(self, file_path):
        data = self.to_dict()
        with open(file_path, 'w') as file:
            json.dump(data, file, indent = 4)

    def load(self, file_path):
        data = {}
        with open(file_path, 'r') as file:
            data = json.load(file)
        for ID, expense_data in data.items():
            expense = Expense(
                expense_data['category'],
                expense_data['amount'],
                expense_data['description'],
                expense_data['date']
            )
            self.expenses[ID] = expense
            expense.set_ID(ID)