import argparse


def add_expenses(args):
    description = args.description
    amount = args.amount
    print(description, amount)

def list_expenses():
    print("List operation working.")


def summarize_expenses():
    print("Summary operation working.")


def delete_expense():
    print("Delete operation working.")


def main() -> None:
    """
    Main function of the program.
    """
    parser = argparse.ArgumentParser(description="Operation argument for expense tracker.")
    subparsers = parser.add_subparsers(dest="operation", required=True)

    # Adding an expense
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", type=str, required=True, help="Description of the expense")
    add_parser.add_argument("--amount", type=float, required=True, help="The amount of the expense")


    args = parser.parse_args()
    operation = args.operation

    match operation:
        case "add":
            add_expenses(args)
        case "list":
            list_expenses()
        case "summary":
            summarize_expenses()
        case "delete":
            delete_expense()
        case _:
            raise ValueError("Invalid operation.")


if __name__ == "__main__":
    main()
