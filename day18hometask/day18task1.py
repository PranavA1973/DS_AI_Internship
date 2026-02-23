import sqlite3
import pandas as pd

conn = sqlite3.connect("interns.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")
cursor.executemany("""
INSERT INTO interns (name, track, stipend)
VALUES (?, ?, ?)
""", [
    ("Aman", "Data Science", 6000),
    ("Riya", "Web Dev", 4000),
    ("Karan", "Data Science", 7000),
    ("Sneha", "Cyber Security", 5500),
    ("Rahul", "Web Dev", 4500),
    ("Priya", "Data Science", 4800),
])
conn.commit()
print("\n--- Data Science Interns with stipend > 5000 ---")
df_filter = pd.read_sql_query("""
SELECT *
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000
""", conn)
print(df_filter)

print("\n--- Average Stipend Per Track ---")
df_avg = pd.read_sql_query("""
SELECT track, AVG(stipend) AS average_stipend
FROM interns
GROUP BY track
""", conn)
print(df_avg)

print("\n--- Intern Count Per Track ---")
df_count = pd.read_sql_query("""
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track
""", conn)
print(df_count)

conn.close()