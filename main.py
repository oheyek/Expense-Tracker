import argparse

def add_expenses():
    print("Add operation working.")

def list_expenses():
    print("List operation working.")

def summarize_expenses():
    print("Summary operation working.")

def delete_expense():
    print("Delete operation working.")

def main() -> None:
    parser = argparse.ArgumentParser(description="Operation argument for expense tracker.")
    parser.add_argument("operation", type=str, help="Operation to perform.")
    operation = parser.parse_args().operation

    match operation:
        case "add":
            add_expenses()
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
