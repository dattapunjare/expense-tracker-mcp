from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("Expense Tracker")

expenses = []


@mcp.tool()
def add_expense(amount: float, category: str, description: str) -> str:
    """Add a new expense to the expense tracker."""
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)

    return (
        f"Expense added successfully: ₹{amount:.2f} "
        f"for {category} - {description}"
    )


@mcp.resource("expense://summary")
def expense_summary() -> str:
    """Provide the current expense summary without modifying expense data."""
    if not expenses:
        return "No expenses have been recorded yet."

    total = sum(expense["amount"] for expense in expenses)

    summary = f"Total expenses: ₹{total:.2f}\n\n"

    for expense in expenses:
        summary += (
            f"- ₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['date']}\n"
        )

    return summary


@mcp.prompt()
def monthly_budget_review() -> str:
    """Provide reusable instructions for reviewing monthly expenses."""
    return """
Review my current expenses and help me understand my spending.

Please:
1. Calculate the total spending.
2. Group expenses by category.
3. Identify the categories with the highest spending.
4. Suggest practical ways to control unnecessary expenses.

Do not invent expenses that are not present in the expense data.
"""


if __name__ == "__main__":
    mcp.run()