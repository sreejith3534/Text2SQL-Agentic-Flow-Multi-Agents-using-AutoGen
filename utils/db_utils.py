import sqlite3
from typing import Annotated, Dict, List, Tuple, Union


def fetch_schema(DB_PATH: Annotated[str, "Path to the Database file"]) -> Annotated[
    str, "Resulting Schema from the DB"]:
    """Fetches the schema of the database (table names, columns, and types)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = {
        table[0]: [
            {"name": col[1], "type": col[2]} for col in cursor.execute(f"PRAGMA table_info({table[0]});").fetchall()
        ]
        for table in tables
    }

    conn.close()
    return "\n".join(
        f"Table: {table}\nColumns: {', '.join(f'{col['name']} ({col['type']})' for col in cols)}"
        for table, cols in schema.items()
    )


def validate_and_execute_sql_query(
        sql_query: Annotated[str, "SQL query from SQLAgent"],
        db_path: Annotated[str, "Path to the Database"]
) -> Annotated[Union[Dict[str, List[Tuple]], str], "Query Result or Error"]:
    """Validates and executes an SQL query."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("EXPLAIN QUERY PLAN " + sql_query)
        cursor.execute(sql_query)

        if sql_query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            conn.close()
            return {"success": results}

        conn.commit()
        conn.close()
    except Exception as e:
        return f"failure: {str(e)}"
