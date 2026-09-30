# Expense Tracker MCP System Design

```mermaid
flowchart TD
    A[MCP Client<br/>MCP Inspector / Claude Desktop]

    A --> B[Tool<br/>add_expense]
    A --> C[Resource<br/>expense://summary]
    A --> D[Prompt<br/>monthly_budget_review]

    B --> E[Expense Data]
    C --> E
    E --> C

    D --> F[Reusable Budget Review Instructions]