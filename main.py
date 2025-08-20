import argparse


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


def add_expenses(args):
    description = args.description
    amount = args.amount
    print(description, amount)


def list_expenses():
    print("List operation working.")


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
