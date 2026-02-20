import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

intern_data = [
    ("Aman", "Data Science", 15000),
    ("Priya", "Web Dev", 12000),
    ("Rahul", "Data Science", 18000),
    ("Sneha", "Web Dev", 10000),
    ("Arjun", "AI/ML", 20000)
]

cursor.executemany(
    "INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)",
    intern_data
)

conn.commit()

cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()

print("Intern Name and Track:")
for row in rows:
    print(row)

conn.close()