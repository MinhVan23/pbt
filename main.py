import sys

from budget import Expense, Budget

def help():
    print(
        'commands:\n'
        '   add <category> <amount> <description> <YYYY-MM-DD> : Add a new expense'
        '   remove <ID>: Remove an expense'
        '       To see IDs of expenses, use "list".'
        '   list: List all expenses in budget'
        '   summary <category> : Get the sum amount of a category'
        '   export <filename> : Export budget as a CSV file'
    )

def main():
    user_budget = Budget() 
    user_budget.load()

    command = sys.argv[1] if len(sys.argv) > 1 else None
    if command == 'add':
        if len(sys.argv) < 6:
            print('Error: enough arguments for expense.')
        category = sys.argv[2]
        amount = sys.argv[3]
        description = sys.argv[4]
        date = sys.argv[5]
        user_budget.add(category, amount, description, date)
    elif command == 'remove':
        if len(sys.argv) < 3:
            print('Error: No ID given to remove expense.')
        ID = sys.argv[3]
        user_budget.remove(ID)
    # implement other commands here
    elif command == 'help' or command == None:
        help()
    else:
        print('Error: Unkown command or incorrect syntax. Use "pbt help" for help!')

    user_budget.save()

if __name__ == '__main__':
    main()