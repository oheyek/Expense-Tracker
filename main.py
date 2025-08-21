import argparse
import json
from datetime import datetime
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
    record_id = max([expense["ID"] for expense in expenses] or [0]) + 1
    new_expense = {"ID": record_id, "Date": datetime.now().strftime("%Y-%m-%d"), "Description": description,
                   "Amount": str(amount)}
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {record_id})")


def list_expenses() -> None:
    """
    Function to read the existing expenses from json file and display it in proper format.
    """
    expenses = load_expenses()
    if not expenses:
        print("There are no expenses yet.")
    else:
        print("ID\t\tDate\t\tDescription\t\tAmount")
        for expense in expenses:
            print(str(expense["ID"]) + "\t\t" + str(expense["Date"]) + "\t\t" + str(
                expense["Description"]) + "\t\t" + f"$" + str(expense["Amount"]))


def summarize_expenses(args: argparse.Namespace) -> str:
    """
    Function to summarize expenses from a file.
    :param args: Arguments for summarize operation.
    :return: Summarized sum of expenses in a specific month if specified otherwise for all months.
    """
    expenses = load_expenses()
    total_expenses = 0
    if expenses:
        if args.month:
            month = args.month
            for index, expense in enumerate(expenses):
                expense_month = int(expense["Date"].split("-")[1])
                if month == expense_month:
                    total_expenses += float(expense["Amount"])
                    date_str = expense["Date"]
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                    month_name = date_obj.strftime("%B")
                    return f"Total expenses for {month_name}: ${total_expenses}"
                else:
                    return "There are no expenses with such a month yet."
        for index, expense in enumerate(expenses):
            total_expenses += float(expense["Amount"])
        return f"Total expenses: ${total_expenses}"
    else:
        return "There are no expenses yet."


def delete_expense(args: argparse.Namespace) -> str:
    """
    Function to delete expense with specific id.
    :param args: Arguments provided by user.
    :return: Message whether the expense has been deleted.
    """
    expense_id = args.id
    expenses = load_expenses()
    for index, expense in enumerate(expenses):
        if expense["ID"] == expense_id:
            expenses.pop(index)
            save_expenses(expenses)
            return "Expense deleted successfully."
    return "There is no such expense with that id."


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
            print(summarize_expenses(args))
        case "delete":
            print(delete_expense(args))
        case _:
            raise ValueError("Invalid operation.")


if __name__ == "__main__":
    main()
