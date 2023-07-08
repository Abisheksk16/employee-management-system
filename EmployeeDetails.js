import React, { useEffect, useState } from 'react';
import axios from 'axios';

const EmployeeDetails = () => {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees = async () => {
    try {
      const response = await axios.get('/employees');
      setEmployees(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Employee Details</h2>
      <ul>
        {employees.map((employee) => (
          <li key={employee._id}>
            <strong>{employee.name}</strong> - {employee.department}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EmployeeDetails;
