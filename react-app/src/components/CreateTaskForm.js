import React, { useState } from 'react';
import { createTask } from '../services/api';

const CreateTaskForm = ({ projectId, onTaskCreated }) => {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    due_date: '',
    priority: 'low',
    status: 'to_do',
    project: projectId,
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    createTask(formData)
      .then((response) => {
        alert('Task created successfully');
        onTaskCreated(response.data);
      })
      .catch((error) => {
        console.error('Error creating task:', error);
        alert('Failed to create task');
      });
  };

  return (
    <form className="container" onSubmit={handleSubmit}>
      <h2>Create Task</h2>
      <input
        type="text"
        name="title"
        placeholder="Task Title"
        value={formData.title}
        onChange={handleChange}
        required
      />
      <textarea
        name="description"
        placeholder="Task Description"
        value={formData.description}
        onChange={handleChange}
      />
      <input
        type="date"
        name="due_date"
        value={formData.due_date}
        onChange={handleChange}
        required
      />
      <select name="priority" value={formData.priority} onChange={handleChange}>
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
        <option value="critical">Critical</option>
      </select>
      <select name="status" value={formData.status} onChange={handleChange}>
        <option value="to_do">To Do</option>
        <option value="in_progress">In Progress</option>
        <option value="review">Review</option>
        <option value="done">Done</option>
      </select>
      <button type="submit">Create Task</button>
    </form>
  );
};

export default CreateTaskForm;
