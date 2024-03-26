import sqlite3
from faker import Faker
import random

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
"""
)

conn.commit()

fake = Faker()

groups = ["Group A", "Group B", "Group C"]
for group_name in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))

teachers = [fake.name() for _ in range(3)]
for teacher_name in teachers:
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher_name,))

subjects = [
    "Math",
    "Physics",
    "Chemistry",
    "Literature",
    "History",
    "Biology",
    "Geography",
]
for subject_name in subjects:
    teacher_id = random.randint(1, len(teachers))
    cursor.execute(
        "INSERT INTO subjects (name, teacher_id) VALUES (?, ?)",
        (subject_name, teacher_id),
    )

for _ in range(30):
    student_name = fake.name()
    group_id = random.randint(1, len(groups))
    cursor.execute(
        "INSERT INTO students (name, group_id) VALUES (?, ?)", (student_name, group_id)
    )

for student_id in range(1, 31):
    for subject_id in range(1, len(subjects) + 1):
        grade = random.randint(1, 10)
        date = fake.date()
        cursor.execute(
            "INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
            (student_id, subject_id, grade, date),
        )

conn.commit()

conn.close()
