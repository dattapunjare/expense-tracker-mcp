# Expense Tracker MCP System Design

                  ┌─────────────────────┐
                  │     MCP Client      │
                  │ Inspector / Claude  │
                  └──────────┬──────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
        ┌────────────┐ ┌────────────┐ ┌────────────────┐
        │    TOOL    │ │  RESOURCE  │ │     PROMPT     │
        │            │ │            │ │                │
        │add_expense │ │expense://  │ │monthly_budget  │
        │            │ │summary     │ │_review        │
        └─────┬──────┘ └─────┬──────┘ └────────────────┘
              │              │
              ▼              ▼
        ┌─────────────────────────┐
        │    Expense Data Store   │
        │      expenses.json      │
        └─────────────────────────┘