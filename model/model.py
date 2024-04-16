from utils.db import Database

class EmployeeModel:
    def __init__(self):
        self.db = Database()

    def fetch_all_employees(self):
        conn = self.db.create_connection()  # Create a new connection
        cur = conn.cursor()  # Create a new cursor
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        conn.close()  # Close the connection
        return rows

    def insert_employee(self, name, age, doj, email, gender, contact, address):
        conn = self.db.create_connection()  # Create a new connection
        cur = conn.cursor()  # Create a new cursor
        cur.execute("INSERT INTO employees (name, age, doj, email, gender, contact, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (name, age, doj, email, gender, contact, address))
        conn.commit()  # Commit the transaction
        conn.close()  # Close the connection

    def update_employee(self, id, name, age, doj, email, gender, contact, address):
        conn = self.db.create_connection()  # Create a new connection
        cur = conn.cursor()  # Create a new cursor
        cur.execute("UPDATE employees SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? WHERE id=?",
                    (name, age, doj, email, gender, contact, address, id))
        conn.commit()  # Commit the transaction
        conn.close()  # Close the connection

    def delete_employee(self, id):
        conn = self.db.create_connection()  # Create a new connection
        cur = conn.cursor()  # Create a new cursor
        cur.execute("DELETE FROM employees WHERE id=?", (id,))
        conn.commit()  # Commit the transaction
        conn.close()  # Close the connection
