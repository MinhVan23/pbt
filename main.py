import sys

import budget

def main():
    user_budget = budget.Budget()

    command = sys.argv[1]
    if command == 'add':
        user_budget.add()

if __name__ == '__main__':
    main()