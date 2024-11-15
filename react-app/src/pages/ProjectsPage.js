import React, { useState } from 'react';
import ProjectList from '../components/ProjectList';
import CreateProjectForm from '../components/CreateProjectForm';

const ProjectsPage = () => {
  const [projects, setProjects] = useState([]);

  const handleProjectCreated = (newProject) => {
    setProjects([...projects, newProject]);
  };

  return (
    <div>
      <h1>Projects</h1>
      <CreateProjectForm onProjectCreated={handleProjectCreated} />
      <ProjectList projects={projects} />
    </div>
  );
};

export default ProjectsPage;
