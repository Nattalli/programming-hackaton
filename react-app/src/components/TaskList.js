import React, { useEffect, useState } from 'react';
import { fetchTasksByProject } from '../services/api';

const TaskList = ({ projectId }) => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (projectId) {
      fetchTasksByProject(projectId)
        .then((response) => {
          setTasks(response.data);
          setLoading(false);
        })
        .catch((error) => {
          console.error('Error fetching tasks:', error);
          setLoading(false);
        });
    }
  }, [projectId]);

  if (loading) {
    return <p>Loading tasks...</p>;
  }

  return (
    <div className="container">
      <h2>Tasks for Project</h2>
      {tasks.length === 0 ? (
        <p>No tasks available for this project.</p>
      ) : (
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <strong>{task.title}</strong> - {task.status}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default TaskList;
