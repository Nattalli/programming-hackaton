import React, { useState } from 'react';
import { createProject } from '../services/api';

const CreateProjectForm = ({ onProjectCreated }) => {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    start_date: '',
    end_date: '',
    status: 'planned',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    createProject(formData)
      .then((response) => {
        alert('Project created successfully');
        onProjectCreated(response.data);
      })
      .catch((error) => {
        console.error('Error creating project:', error);
        alert('Failed to create project');
      });
  };

  return (
    <form className="container" onSubmit={handleSubmit}>
      <h2>Create Project</h2>
      <input
        type="text"
        name="name"
        placeholder="Project Name"
        value={formData.name}
        onChange={handleChange}
        required
      />
      <textarea
        name="description"
        placeholder="Project Description"
        value={formData.description}
        onChange={handleChange}
      />
      <input
        type="date"
        name="start_date"
        value={formData.start_date}
        onChange={handleChange}
        required
      />
      <input
        type="date"
        name="end_date"
        value={formData.end_date}
        onChange={handleChange}
      />
      <select name="status" value={formData.status} onChange={handleChange}>
        <option value="planned">Planned</option>
        <option value="in_progress">In Progress</option>
        <option value="completed">Completed</option>
        <option value="archived">Archived</option>
      </select>
      <button type="submit">Create Project</button>
    </form>
  );
};

export default CreateProjectForm;
