import sqlite3
import pandas as pd
import os

# 1. Load the CSV file
# 'on_bad_lines' skips any malformed rows in the dataset
print("Loading car_prices.csv...")
df = pd.read_csv("car_prices.csv", on_bad_lines='skip')

# 2. Clean the Column Names (Critical for SQL)
# This removes spaces so the AI doesn't get confused (e.g., "selling price" -> "selling_price")
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# 3. Connect to a new database file
db_name = "car_sales.db"
connection = sqlite3.connect(db_name)

# 4. Dump Data into SQL
# This automatically creates the table 'cars' and inserts all 500k+ rows
print("Converting CSV to SQL Table...")
df.to_sql('cars', connection, if_exists='replace', index=False)

# 5. Verify it worked
cursor = connection.cursor()
print("Data loaded successfully! Preview of first 3 rows:")
data = cursor.execute('''SELECT * FROM cars LIMIT 3''')
for row in data:
    print(row)

# 6. Close
connection.commit()
connection.close()
print(f"Database {db_name} created successfully.")