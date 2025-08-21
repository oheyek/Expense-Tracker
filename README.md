# 💰 Expense Tracker CLI

A sleek, lightweight command-line expense management tool built with Python. Keep track of your spending with simple
commands and JSON-based storage.

## ✨ Features

- **Simple & Fast**: Add, list, summarize, and delete expenses with single commands
- **Automatic ID Management**: Auto-incrementing expense IDs for easy reference
- **Date Tracking**: Automatic date assignment for every expense
- **Monthly Summaries**: View expenses by specific month or overall totals
- **JSON Storage**: Human-readable expense storage in `expenses.json`
- **Flexible Filtering**: Summarize expenses by month or view all expenses
- **Error Handling**: Robust input validation and helpful error messages

## 🛠️ Installation

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/oheyek/Expense-Tracker-CLI.git
cd Expense-Tracker-CLI

# Install dependencies
pip install -r requirements.txt

# Install as a CLI tool (optional)
pip install -e .
```

### Using as Installed CLI

After installation, you can use `expense-tracker` directly:

```bash
expense-tracker add --description "Lunch" --amount 20
```

### Using Python Script

Alternatively, run directly with Python:

```bash
python main.py add --description "Lunch" --amount 20
```

## 🎯 Usage

### Adding Expenses

```bash
# Add a new expense
expense-tracker add --description "Lunch" --amount 20
expense-tracker add --description "Coffee" --amount 5.50
expense-tracker add --description "Gas" --amount 45.75
```

### Listing Expenses

```bash
# List all expenses
expense-tracker list
```

### Summarizing Expenses

```bash
# Get total of all expenses
expense-tracker summary

# Get total for a specific month (1-12)
expense-tracker summary --month 8
expense-tracker summary --month 12
```

### Deleting Expenses

```bash
# Delete an expense by ID
expense-tracker delete --id 1
```

## 📋 Command Reference

| Command   | Arguments                                | Description                           | Example                                                        |
|-----------|------------------------------------------|---------------------------------------|----------------------------------------------------------------|
| `add`     | `--description <text> --amount <number>` | Add a new expense                     | `expense-tracker add --description "Groceries" --amount 85.50` |
| `list`    | None                                     | List all expenses                     | `expense-tracker list`                                         |
| `summary` | `[--month <1-12>]`                       | Show expense totals (all or by month) | `expense-tracker summary --month 3`                            |
| `delete`  | `--id <number>`                          | Delete an expense by ID               | `expense-tracker delete --id 5`                                |

## 🔥 Complete Example Workflow

```bash
# Add some expenses
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker add --description "Coffee" --amount 4.50
# Expense added successfully (ID: 3)

# List all expenses
$ expense-tracker list
# ID		Date		Description		Amount
# 1		2024-08-06	Lunch			$20
# 2		2024-08-06	Dinner			$10
# 3		2024-08-06	Coffee			$4.5

# Get total summary
$ expense-tracker summary
# Total expenses: $34.5

# Delete an expense
$ expense-tracker delete --id 2
# Expense deleted successfully

# Check updated summary
$ expense-tracker summary
# Total expenses: $24.5

# Get monthly summary
$ expense-tracker summary --month 8
# Total expenses for August: $24.5
```

## 📊 Expense Structure

Each expense is stored with the following structure:

```json
{
  "ID": 1,
  "Date": "2024-08-06",
  "Description": "Lunch",
  "Amount": "20.0"
}
```

## 🗂️ File Structure

```
Expense-Tracker-CLI/
├── main.py           # Main application logic
├── expenses.json     # Expense storage (auto-generated)
├── requirements.txt  # Python dependencies
├── setup.py         # Package setup configuration
└── README.md        # This file
```

## 🔧 Technical Details

- **Language**: Python 3.8+
- **Storage**: JSON file-based persistence
- **Dependencies**: Standard library (argparse, json, datetime)
- **Error Handling**: Comprehensive input validation
- **ID Management**: Auto-incrementing expense IDs
- **Date Format**: YYYY-MM-DD (ISO format)

## 🚦 Error Handling

The CLI provides helpful error messages for common scenarios:

- **No expenses found**: "There are no expenses yet."
- **Invalid ID**: "There is no such expense with that id."
- **No monthly expenses**: "There are no expenses with such a month yet."
- **Missing arguments**: Detailed argument requirement messages

## 💡 Features in Detail

### Smart ID Management

- Automatically assigns unique, incrementing IDs
- Handles ID gaps after deletions
- Starts from ID 1 for the first expense

### Date Handling

- Automatically assigns current date to new expenses
- Uses ISO format (YYYY-MM-DD) for consistency
- Monthly filtering based on expense date

### Amount Formatting

- Supports decimal amounts (e.g., 15.50)
- Displays amounts with $ prefix
- Stores as string for precision

### Monthly Summaries

- Month parameter accepts numbers 1-12
- Displays full month name (e.g., "August" for month 8)
- Calculates totals only for matching month

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📈 Use Cases

### Personal Finance Tracking

```bash
# Daily expenses
expense-tracker add --description "Morning coffee" --amount 3.50
expense-tracker add --description "Lunch at work" --amount 12.00
expense-tracker add --description "Grocery shopping" --amount 67.85

# Weekly review
expense-tracker list
expense-tracker summary
```

### Monthly Budget Management

```bash
# Track January expenses
expense-tracker summary --month 1

# Compare with February
expense-tracker summary --month 2

# View annual total
expense-tracker summary
```

### Expense Categories

```bash
# Food expenses
expense-tracker add --description "Restaurant dinner" --amount 45.00
expense-tracker add --description "Groceries - weekly" --amount 120.50

# Transportation
expense-tracker add --description "Gas fill-up" --amount 55.00
expense-tracker add --description "Subway card" --amount 20.00
```

## ⚡ Performance Notes

- Lightweight JSON storage
- Fast file-based operations
- Minimal memory footprint
- Instant command execution

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Expense Tracking! 💸**

## Author

Made with ❤️ by ohey<br>
[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/black_img.png)](https://www.buymeacoffee.com/ohey)

---

If you find this project useful, consider buying me a coffee!

https://roadmap.sh/projects/expense-tracker
