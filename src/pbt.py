import sys
import os

from budget import Budget

default_export_directory = os.path.expanduser('~/pbt/exports')
data_path = os.path.expanduser('~/pbt/data.json')

def help():
    print("""
Usage: pbt <command> <arguments>
Commands:
    add <category> <amount> <description> <YYYY-MM-DD>  Add a new expense
    remove <ID>                                         Remove an expense
                                                        To see IDs of expenses, use "list".
    list                                                List all expenses in budget
    summary <category>                                  Get the sum amount of a category
    export <filename> [directory]                       Export budget as a CSV file
"""
    )

def main():
    user_budget = Budget() 
    if os.path.exists(data_path):
        user_budget.load(data_path)

    command = sys.argv[1] if len(sys.argv) > 1 else None
    args = sys.argv[2:]
    if command == 'add':
        if len(args) < 4:
            print('Error: enough arguments for expense.')
        category = args[0]
        amount = float(args[1])
        description = args[2]
        date = args[3]
        user_budget.add(category, amount, description, date)
    elif command == 'remove':
        ID = args[0] if len(args) > 0 else None
        if not ID:
            print('Error: No ID given to remove expense.')
            return
        user_budget.remove(ID)
    elif command == 'list':
        user_budget.list_expenses()
    elif command == 'summary':
        category = args[0] if len(args) > 0 else None
        if not category:
            print('Error: no category given to summarised.')
            return
        user_budget.summary(category)
    elif command == 'export':
        filename = args[0] if len(args) > 0 else None
        directory = args[1] if len(args) >1 else default_export_directory
        if not filename:
            print('Error: filename need to be specified.')
            return
        if not directory:
            print(f'No directory was given. Export will be in default export directory: {default_export_directory}.')
        user_budget.export_csv(filename, directory)
    elif command == 'help' or command == None:
        help()
    else:
        print('Error: Unkown command or incorrect syntax. Use "pbt help" for help!')

    user_budget.save(data_path)

if __name__ == '__main__':
    main()