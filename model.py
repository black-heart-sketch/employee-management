from db import Database

class EmployeeModel:
    def __init__(self):
        self.db = Database("Employee.db")

    def fetch_all_employees(self):
        return self.db.fetch()

    def insert_employee(self, name, age, doj, email, gender, contact, address):
        self.db.insert(name, age, doj, email, gender, contact, address)

    def update_employee(self, id, name, age, doj, email, gender, contact, address):
        self.db.update(id, name, age, doj, email, gender, contact, address)

    def delete_employee(self, id):
        self.db.remove(id)
