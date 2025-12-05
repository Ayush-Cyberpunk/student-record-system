import sqlite3


conn = sqlite3.connect('student.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS students (
    roll TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    branch TEXT NOT NULL
)
''')
conn.commit()

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    try:
        c.execute(
            "INSERT INTO students (roll, name, branch) VALUES (?, ?, ?)",
            (roll, name, branch)
        )
        conn.commit()
        print("✅ Student added!\n")
    except sqlite3.IntegrityError:
        print("⚠ Roll number already exists.\n")

def view_students():
    print("\n--- All Students ---")
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    if not rows:
        print("No records found.\n")
    else:
        for r, n, b in rows:
            print(f"Roll: {r}, Name: {n}, Branch: {b}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    c.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    student = c.fetchone()
    if student:
        print(f"Found → Roll: {student[0]}, Name: {student[1]}, Branch: {student[2]}\n")
    else:
        print("❌ Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    c.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    if c.fetchone():
        name = input("New Name: ")
        branch = input("New Branch: ")
        c.execute(
            "UPDATE students SET name = ?, branch = ? WHERE roll = ?",
            (name, branch, roll)
        )
        conn.commit()
        print("✅ Student updated!\n")
    else:
        print("❌ Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    c.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    if c.fetchone():
        c.execute("DELETE FROM students WHERE roll = ?", (roll,))
        conn.commit()
        print("✅ Student deleted!\n")
    else:
        print("❌ Student not found.\n")

def main():
    while True:
        print("===== Student Record System (SQLite) =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Choose (1–6): ")
        if choice == "1": add_student()
        elif choice == "2": view_students()
        elif choice == "3": search_student()
        elif choice == "4": update_student()
        elif choice == "5": delete_student()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("⚠ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
    conn.close()
