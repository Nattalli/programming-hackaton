import React, { useEffect, useState } from 'react';
import { fetchProjects } from '../services/api';
import { Link } from 'react-router-dom';

const ProjectList = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetchProjects()
      .then((response) => setProjects(response.data))
      .catch((error) => console.error('Error fetching projects:', error));
  }, []);

  return (
    <div className="container">
      <h2>Projects</h2>
      <ul>
        {projects.map((project) => (
          <li key={project.id}>
            <strong>{project.name}</strong> - {project.status}{' '}
            <Link to={`/projects/${project.id}`}>View Details</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProjectList;
