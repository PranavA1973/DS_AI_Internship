import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    intern_id INTEGER PRIMARY KEY,
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
])
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")
cursor.executemany("""
INSERT INTO mentors (mentor_name, track)
VALUES (?, ?)
""", [
    ("Dr. Mehta", "Data Science"),
    ("Mr. Kapoor", "Web Dev"),
    ("Ms. Iyer", "Cyber Security"),
])

conn.commit()
query = """
SELECT 
    i.name AS intern_name,
    i.track,
    i.stipend,
    m.mentor_name
FROM interns i
INNER JOIN mentors m
ON i.track = m.track
"""

df = pd.read_sql_query(query, conn)

print("\n--- Interns with Their Mentors ---")
print(df)

conn.close()