# Expense Tracker MCP Server

This project is an MCP-based expense tracker built using FastMCP. It allows an AI assistant to add expenses, read the current expense summary, and use a reusable prompt to review monthly spending.

## MCP Primitives

### 1. Tool - add_expense

The `add_expense` tool adds a new expense to the tracker.

A tool is used because adding an expense is an action that changes the stored expense data. The model can decide when this action should be performed based on the user's request.

### 2. Resource - expense://summary

The `expense://summary` resource provides the current expense summary.

A resource is used because it provides addressable data that the client can read without performing an action or changing the expense data.

### 3. Prompt - monthly_budget_review

The `monthly_budget_review` prompt provides reusable instructions for reviewing expenses.

A prompt is used because it is an instruction template that the user can intentionally select when they want to review their spending.

## Project Structure

- `server.py` - Contains the FastMCP server, tool, resource, and prompt.
- `README.md` - Explains the project and the design choices.
- `pyproject.toml` - Contains the project configuration and dependency.
- `.gitignore` - Specifies files that should not be committed to Git.