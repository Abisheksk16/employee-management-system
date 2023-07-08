from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
from bson.json_util import dumps
import json

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/employee_management'
mongo = PyMongo(app)

# Custom JSON Encoder to handle ObjectId serialization
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)
# Employee Details Endpoints
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = list(mongo.db.employees.find())
    return jsonify(employees), 200

@app.route('/employees', methods=['POST'])
def create_employee():
    employee_data = request.get_json()
    result = mongo.db.employees.insert_one(employee_data)
    if result.inserted_id:
        return jsonify({'message': 'Employee created', 'employee_id': str(result.inserted_id)}), 201
    else:
        return jsonify({'message': 'Failed to create employee'}), 500

@app.route('/employees/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = mongo.db.employees.find_one({'_id': ObjectId(employee_id)})
    if employee:
        return jsonify(employee), 200
    else:
        return jsonify({'message': 'Employee not found'}), 404

@app.route('/employees/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee_data = request.get_json()
    result = mongo.db.employees.update_one({'_id': ObjectId(employee_id)}, {'$set': employee_data})
    if result.modified_count > 0:
        return jsonify({'message': 'Employee updated'}), 200
    else:
        return jsonify({'message': 'Employee not found'}), 404

@app.route('/employees/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    result = mongo.db.employees.delete_one({'_id': ObjectId(employee_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Employee deleted'}), 200
    else:
        return jsonify({'message': 'Employee not found'}), 404

# Department Details Endpoints
@app.route('/departments', methods=['GET'])
def get_departments():
    departments = list(mongo.db.departments.find())
    return jsonify(departments), 200

@app.route('/departments', methods=['POST'])
def create_department():
    department_data = request.get_json()
    result = mongo.db.departments.insert_one(department_data)
    if result.inserted_id:
        return jsonify({'message': 'Department created', 'department_id': str(result.inserted_id)}), 201
    else:
        return jsonify({'message': 'Failed to create department'}), 500

@app.route('/departments/<department_id>', methods=['GET'])
def get_department(department_id):
    department = mongo.db.departments.find_one({'_id': ObjectId(department_id)})
    if department:
        return jsonify(department), 200
    else:
        return jsonify({'message': 'Department not found'}), 404

@app.route('/departments/<department_id>', methods=['PUT'])
def update_department(department_id):
    department_data = request.get_json()
    result = mongo.db.departments.update_one({'_id': ObjectId(department_id)}, {'$set': department_data})
    if result.modified_count > 0:
        return jsonify({'message': 'Department updated'}), 200
    else:
        return jsonify({'message': 'Department not found'}), 404

@app.route('/departments/<department_id>', methods=['DELETE'])
def delete_department(department_id):
    result = mongo.db.departments.delete_one({'_id': ObjectId(department_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Department deleted'}), 200
    else:
        return jsonify({'message': 'Department not found'}), 404

# Employee-Department Assignment
@app.route('/employees/<employee_id>/assign', methods=['PUT'])
def assign_employee_to_department(employee_id):
    department_id = request.json.get('department_id')
    department = mongo.db.departments.find_one({'_id': ObjectId(department_id)})
    if not department:
        return jsonify({'message': 'Department not found'}), 404
    result = mongo.db.employees.update_one({'_id': ObjectId(employee_id)}, {'$set': {'department_id': department_id}})
    if result.modified_count > 0:
        return jsonify({'message': 'Employee assigned to department'}), 200
    else:
        return jsonify({'message': 'Employee not found'}), 404

# Employee Promotion
@app.route('/employees/<employee_id>/promote', methods=['PUT'])
def promote_employee(employee_id):
    employee = mongo.db.employees.find_one({'_id': ObjectId(employee_id)})
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    experience_years = employee.get('years_of_experience', 0)
    if experience_years >= 5:
        result = mongo.db.employees.update_one({'_id': ObjectId(employee_id)}, {'$set': {'role': 'manager'}})
        if result.modified_count > 0:
            return jsonify({'message': 'Employee promoted to manager'}), 200
    return jsonify({'message': 'Employee not eligible for promotion'}), 400

if __name__ == '__main__':
    app.run(debug=True)
