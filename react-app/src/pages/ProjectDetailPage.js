import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import TaskList from '../components/TaskList';
import CreateTaskForm from '../components/CreateTaskForm';

const ProjectDetailPage = () => {
  const { projectId } = useParams();
  const [tasks, setTasks] = useState([]);

  const handleTaskCreated = (newTask) => {
    setTasks([...tasks, newTask]);
  };

  return (
    <div>
      <h1>Project Details</h1>
      <CreateTaskForm projectId={projectId} onTaskCreated={handleTaskCreated} />
      <TaskList tasks={tasks} />
    </div>
  );
};

export default ProjectDetailPage;
