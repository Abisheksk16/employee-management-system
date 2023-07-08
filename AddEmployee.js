import React, { useState } from 'react';
import axios from 'axios';

const AddEmployee = () => {
  const [employeeData, setEmployeeData] = useState({
    name: '',
    department: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEmployeeData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    axios.post('/employees', employeeData)
      .then((response) => {
        console.log(response.data.message);
        // Handle success, e.g., show success message, reset form, etc.
      })
      .catch((error) => {
        console.error(error);
        // Handle error, e.g., show error message, etc.
      });

    // Reset the form
    setEmployeeData({
      name: '',
      department: '',
    });
  };

  return (
    <div>
      <h2>Add Employee</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={employeeData.name}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="department">Department:</label>
          <input
            type="text"
            id="department"
            name="department"
            value={employeeData.department}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit">Add Employee</button>
      </form>
    </div>
  );
};

export default AddEmployee;
