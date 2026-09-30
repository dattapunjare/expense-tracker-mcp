# Expense Tracker MCP

## Overview

Expense Tracker MCP is a small local Model Context Protocol (MCP) server developed using FastMCP. The project demonstrates how an AI application can interact with structured expense data through MCP primitives.

The server provides three core MCP primitives: a tool, a resource, and a prompt. Each primitive has a different purpose and demonstrates how MCP separates actions, data access, and reusable instructions.


How It Works:

The Expense Tracker stores expenses in memory while the server is running. Each expense contains an amount, category, description, and date.

The AI client can interact with the server in three ways:

Tool - add_expense

The add_expense tool is used to add a new expense.

It accepts:

Amount
Category
Description

When the tool is called, the new expense is added to the expense data.

Resource - expense://summary

The expense://summary resource provides the current expense information.

It calculates the total spending and displays the recorded expenses. Reading the resource does not modify the stored expense data.

Prompt - monthly_budget_review

The monthly_budget_review prompt provides reusable instructions for reviewing expenses.

It guides an AI assistant to:

Calculate total spending.
Group expenses by category.
Identify categories with the highest spending.
Suggest practical ways to control unnecessary expenses.


## Design Approach

The project follows a simple separation of responsibilities:

MCP Client
    |
    v
Expense Tracker MCP Server
    |
    +---- Tool ----> Add Expense
    |
    +---- Resource -> Read Expense Summary
    |
    +---- Prompt --> Review Spending Instructions


## Project Structure

- `server.py` - Contains the MCP server, tool, resource, and prompt.
- `README.md` - Explains the project and the design choices.
- `pyproject.toml` - Contains the project configuration and dependency.
- `.gitignore` - Specifies files that should not be committed to Git.


## Testing

The server was tested using MCP Inspector.

All three primitives were verified:

add_expense successfully added expenses.
expense://summary successfully displayed the recorded expenses and total spending.
monthly_budget_review successfully returned the reusable budget-review instructions.


