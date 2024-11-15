import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
});

export const fetchProjects = () => API.get('/projects/');
export const fetchTasksByProject = (projectId) => API.get(`/tasks/?project=${projectId}`);
export const fetchWorkflows = () => API.get('/workflows/');

export const createProject = (data) => API.post('/projects/', data);
export const createTask = (data) => API.post('/tasks/', data);
export const createWorkflow = (data) => API.post('/workflows/', data);
