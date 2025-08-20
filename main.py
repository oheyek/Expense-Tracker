import argparse


def main() -> None:
    """
    Main function of the program.
    """
    parser = argparse.ArgumentParser(description="Test for expense tracker arg parsing.")
    parser.add_argument("operation", type=str, help="Test operation")
    arg = parser.parse_args()
    print(arg.operation)
    if arg.operation == "test":
        print("CLI Test.")

if __name__ == "__main__":
    main()
