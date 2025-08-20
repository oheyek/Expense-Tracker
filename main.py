import argparse
import datetime
import json
from typing import List


def load_args() -> argparse.Namespace:
    """
    Function to load arguments provided by user from CLI.
    :return: User's command arguments.
    """
    parser = argparse.ArgumentParser(description="Operation argument for expense tracker.")
    subparsers = parser.add_subparsers(dest="operation", required=True)

    # Adding an expense
    add_parser = subparsers.add_parser("add", help="Add a new expense.")
    add_parser.add_argument("--description", type=str, required=True, help="Description of the expense.")
    add_parser.add_argument("--amount", type=float, required=True, help="The amount of the expense.")

    # List expenses
    subparsers.add_parser("list", help="List existing expenses.")

    # Summarize expenses
    summary_parser = subparsers.add_parser("summary", help="Summarize expenses.")
    summary_parser.add_argument("--month", type=int, required=False, help="Summarize expenses at specific month.")

    # Delete expense
    delete_parser = subparsers.add_parser("delete", help="Delete expense.")
    delete_parser.add_argument("--id", type=int, required=True, help="Id of expense to be deleted.")

    args = parser.parse_args()
    return args


def load_expenses() -> List:
    """
    Function to load expenses from a file.
    :return: List for a loaded expenses.
    """
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses: List) -> None:
    """
    Function to save expenses to a file.
    :param expenses: Task list to be saved.
    """
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def add_expenses(args: argparse.Namespace) -> None:
    """
    Function to add expenses to the json file.
    :param args: Arguments for adding an expense.
    """
    description = args.description
    amount = args.amount
    expenses = load_expenses()
    record_id = max((expense["ID"] for expense in expenses), default=0) + 1
    new_expense = {"ID": record_id, "Date": datetime.datetime.now().strftime("%Y-%m-%d"), "Description": description,
        "Amount": f"$" + str(amount)}
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {record_id})")


def list_expenses() -> None:
    """
    Function to read the existing expenses from json file and display it in proper format.
    """
    expenses = load_expenses()
    print("ID\t\tDate\t\tDescription\t\tAmount")
    for expense in range(len(expenses)):
        print(str(expenses[expense]["ID"]) + "\t\t" + str(expenses[expense]["Date"]) + "\t\t" + str(
            expenses[expense]["Description"]) + "\t\t" + str(expenses[expense]["Amount"]))


def summarize_expenses(args):
    if args.month:
        month = args.month
        print(month)
    print("Summary operation working.")


def delete_expense(args):
    expense_id = args.id
    print(expense_id)
    print("Delete operation working.")


def main() -> None:
    """
    Main function of the program.
    """
    args = load_args()
    operation = args.operation

    match operation:
        case "add":
            add_expenses(args)
        case "list":
            list_expenses()
        case "summary":
            summarize_expenses(args)
        case "delete":
            delete_expense(args)
        case _:
            raise ValueError("Invalid operation.")


if __name__ == "__main__":
    main()
