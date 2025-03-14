# Text2SQL Agentic Flow (Multi Agents) using AutoGen

** Make use of "Agent Chat Manager Flow" jupyter notebook file for now, as it is more clear to understand **
## Overview
This project implements an agentic flow using Microsoft AutoGen to convert natural language queries into SQL queries. The agents work collaboratively to understand the query, extract database schema, generate and validate SQL, correct errors if needed, and format the results.

## Dataset & Database Setup
We use the **Blinkit Sales Dataset** from Kaggle: [Blinkit Sales Dataset](https://www.kaggle.com/datasets/akxiit/blinkit-sales-dataset?resource=download).

To create a database from the dataset (CSV/XLSX files), use the `deb_prep.py` script. It processes the dataset and initializes the SQLite database.

## Folder Structure
```
text2sql_project/
│── main.py                      # Entry point for execution
│── config.py                     # Configurations and constants
│── deb_prep.py                   # Script to create SQLite DB from CSV/XLSX
│── agents/
│   │── __init__.py               # Init file for package import
│   │── user_proxy.py              # UserProxy agent
│   │── schema_agent.py            # Schema extraction agent
│   │── sql_agent.py               # SQL generation agent
│   │── validation_agent.py        # Query validation agent
│   │── sql_error_correction.py    # SQL error correction agent
│   │── result_formatting.py       # Result formatting agent
│── utils/
│   │── __init__.py               # Init file for package import
│   │── db_utils.py                # Functions to interact with SQLite
│── autogen_setup.py              # AutoGen setup with agents and group chat
│── requirements.txt              # Dependencies
│── README.md                     # Project documentation
```

## Agent Workflow
### **1. UserProxy Agent**
- Acts as the interface for user queries.
- Passes the query to the **SchemaAgent**.

### **2. SchemaAgent**
- Extracts database schema using `fetch_schema(DB_PATH)`.
- Determines relevant tables for query execution.

### **3. SQLAgent**
- Generates an optimized SQL query based on the user request and extracted schema.

### **4. ValidationAgent**
- Validates the generated SQL using `validate_and_execute_sql_query()`.
- If successful, it passes the results to the **ResultFormattingAgent**.
- If errors occur, it sends the query to **SQLErrorCorrectionAgent**.

### **5. SQLErrorCorrectionAgent**
- Analyzes errors and corrects the SQL query.
- Sends the corrected SQL back to **ValidationAgent**.

### **6. ResultFormattingAgent**
- Formats the query output for better readability.
- Provides the final response to the user.

## Installation & Setup
1. **Clone the Repository**
```bash
git clone <repo-url>
cd project
```
2. **Install Dependencies**
```bash
pip install -r requirements.txt
```
3. **Prepare the Database**
```bash
python deb_prep.py
```
4. **Run the Application**
```bash
python main.py
```

## Usage
1. Enter a natural language query related to sales data.
2. The agents will process the request and return an SQL query result.

## Example Query & Output
**User Query:** _"Show me the total sales for each product in the last month."_

**Generated SQL Query:**
```sql
SELECT product_name, SUM(sales_amount)
FROM sales_data
WHERE sales_date >= date('now', '-1 month')
GROUP BY product_name;
```

**Formatted Output:**
| Product Name | Total Sales |
|-------------|------------|
| Product A   | $10,000    |
| Product B   | $8,500     |


Note:
for ease I have put two notebooks:
1. Agent Manual Interaction - where the flow of agents is manual in nature and you can understand about each agent and how they communicate.
2. Agent Chat Manager Flow - the above agent workflow combined in one notebook for you to give a try.

Happy Coding :)

