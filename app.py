from flask import Flask, jsonify, request
from controller.controller import EmployeeController

app = Flask(__name__)
employee_controller = EmployeeController()

@app.route('/employees', methods=['GET'])
def get_all_employees():
    employees = employee_controller.get_all_employees()
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    employee_controller.add_employee(data['name'], data['age'], data['doj'], data['email'], data['gender'], data['contact'], data['address'])
    return jsonify({'message': 'Employee added successfully'})

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    employee_controller.update_employee(id, data['name'], data['age'], data['doj'], data['email'], data['gender'], data['contact'], data['address'])
    return jsonify({'message': 'Employee updated successfully'})

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee_controller.delete_employee(id)
    return jsonify({'message': 'Employee deleted successfully'})

if __name__ == '__main__':
    app.run(debug=False, port=5000)
