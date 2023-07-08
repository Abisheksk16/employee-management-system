import React, { useState, useEffect } from 'react';
import { Switch } from 'react-router-dom';
import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Replace with your backend API URL

function App() {
  const [employees, setEmployees] = useState([]);
  const [departments, setDepartments] = useState([]);
  const [newEmployee, setNewEmployee] = useState({
    name: '',
    email: '',
    contactNumber: '',
  });

  // Fetch employees and departments data from the backend API
  useEffect(() => {
    getEmployees();
    getDepartments();
  }, []);

  // Fetch all employees
  const getEmployees = async () => {
    try {
      const response = await axios.get(`${API_URL}/employees`);
      setEmployees(response.data);
    } catch (error) {
      console.error('Error fetching employees:', error);
    }
  };

  // Fetch all departments
  const getDepartments = async () => {
    try {
      const response = await axios.get(`${API_URL}/departments`);
      setDepartments(response.data);
    } catch (error) {
      console.error('Error fetching departments:', error);
    }
  };

  // Handle input changes in the employee creation form
  const handleEmployeeInputChange = (event) => {
    const { name, value } = event.target;
    setNewEmployee((prevEmployee) => ({
      ...prevEmployee,
      [name]: value,
    }));
  };

  // Handle employee creation form submission
  const handleEmployeeSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(`${API_URL}/employees`, newEmployee);
      const createdEmployee = response.data;
      setEmployees((prevEmployees) => [...prevEmployees, createdEmployee]);
      setNewEmployee({
        name: '',
        email: '',
        contactNumber: '',
      });
    } catch (error) {
      console.error('Error creating employee:', error);
    }
  };

  return (
    <div>
      <h1>Employee Management System</h1>
      
      <h2>Employees</h2>
      <table>
        {/* ... */}
      </table>
      
      <h2>Add Employee</h2>
      <form onSubmit={handleEmployeeSubmit}>
        <label>
          Name:
          <input
            type="text"
            name="name"
            value={newEmployee.name}
            onChange={handleEmployeeInputChange}
          />
        </label>
        <label>
          Email:
          <input
            type="email"
            name="email"
            value={newEmployee.email}
            onChange={handleEmployeeInputChange}
          />
        </label>
        <label>
          Contact Number:
          <input
            type="text"
            name="contactNumber"
            value={newEmployee.contactNumber}
            onChange={handleEmployeeInputChange}
          />
        </label>
        <button type="submit">Add Employee</button>
      </form>
      
      <h2>Departments</h2>
      <table>
        {/* ... */}
      </table>
    </div>
  );
}

export default App;
