import os
import pandas as pd
import sqlite3


def import_csv_to_db(file_path, conn):
    """Imports a CSV file into SQLite database."""
    table_name = os.path.splitext(os.path.basename(file_path))[0]
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Imported {file_path} into {table_name} table.")


def import_excel_to_db(file_path, conn):
    """Imports an Excel file (all sheets) into SQLite database."""
    xls = pd.ExcelFile(file_path)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        table_name = f"{base_name}_{sheet_name}"
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Imported {file_path} (Sheet: {sheet_name}) into {table_name} table.")


def import_files_to_db(dataset_path, db_name):
    """Imports all CSV and Excel files from a directory into SQLite database."""
    conn = sqlite3.connect(db_name)

    for file_name in os.listdir(dataset_path):
        file_path = os.path.join(dataset_path, file_name)

        if file_name.endswith('.csv'):
            import_csv_to_db(file_path, conn)
        elif file_name.endswith('.xlsx'):
            import_excel_to_db(file_path, conn)

    conn.close()
    print("All files imported successfully into", db_name)


if __name__ == "__main__":
    dataset_path = 'blinkit_dataset'
    db_name = 'blinkit_sales.db'
    import_files_to_db(dataset_path, db_name)
